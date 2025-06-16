import tkinter as tk
from tkinter import filedialog
import re

memory = [0] * 256
registers = {"A": 0, "B": 0, "C": 0, "D": 0}
flags = {"Z": 0}
pc = 0
running = True
instr_map = {}
active_regs = []
active_mem = []

opcode = {
    "MOV": 1, "ADD": 2, "JMP": 3, "HLT": 4,
    "SUB": 5, "INC": 6, "DEC": 7, "JNZ": 8, "PRINT": 9
}

def bitstr(val): return f"{val:08b}"

def fetch():
    global pc
    val = memory[pc]
    active_mem.append(pc)
    pc += 1
    return val

def decode_execute(instr):
    global running, pc
    active_regs.clear()
    if instr == 1:
        reg = chr(fetch()); val = fetch()
        registers[reg] = val; active_regs.append(reg)
        flags["Z"] = int(registers[reg] == 0)
    elif instr == 2:
        r1 = chr(fetch()); r2 = chr(fetch())
        registers[r1] = (registers[r1] + registers[r2]) & 0xFF
        active_regs.extend([r1, r2])
        flags["Z"] = int(registers[r1] == 0)
    elif instr == 3:
        addr = fetch()
        pc = addr
    elif instr == 4:
        running = False
    elif instr == 5:
        r1 = chr(fetch()); r2 = chr(fetch())
        registers[r1] = (registers[r1] - registers[r2]) & 0xFF
        active_regs.extend([r1, r2])
        flags["Z"] = int(registers[r1] == 0)
    elif instr == 6:
        r = chr(fetch())
        registers[r] = (registers[r] + 1) & 0xFF
        active_regs.append(r)
        flags["Z"] = int(registers[r] == 0)
    elif instr == 7:
        r = chr(fetch())
        registers[r] = (registers[r] - 1) & 0xFF
        active_regs.append(r)
        flags["Z"] = int(registers[r] == 0)
    elif instr == 8:
        reg = chr(fetch())
        addr = fetch()
        if registers.get(reg, 0) != 0:
            pc = addr
    elif instr == 9:
        r = chr(fetch())
        val = registers.get(r, 0)
        output_box.insert(tk.END, f"{r} = {val}\n")
        output_box.see(tk.END)

def step():
    global running
    if not running: return
    instr_addr = pc
    instr = fetch()
    decode_execute(instr)
    update_gui(instr_addr)

def update_gui(current_instr=None):
    for r in registers:
        color = "yellow" if r in active_regs else "white"
        reg_labels[r].config(text=bitstr(registers[r]), bg=color)
    for i in range(32):
        bg = "lightgreen" if i in active_mem else "white"
        mem_labels[i][1].config(text=bitstr(memory[i]), bg=bg)
        mem_labels[i][0].config(bg=bg)
        prog_labels[i].config(text=f"{i:03} (0x{i:02X}): {memory[i]:02X}", bg=bg)
    active_mem.clear()
    pc_label.config(text=f"PC: {pc:03}")
    flag_label.config(text=f"Z: {flags['Z']}")
    opcode_label.config(text=f"OP: {memory[current_instr]:02X}" if current_instr is not None else "OP: -")
    asm_editor.tag_remove("highlight", "1.0", tk.END)
    if current_instr in instr_map:
        lineno = instr_map[current_instr]
        asm_editor.tag_add("highlight", f"{lineno}.0", f"{lineno}.end")

def compile_asm(src: str) -> list:
    global instr_map
    lines = [l.rstrip() for l in src.splitlines()]
    labels = {}
    bytecode = []
    instr_map = {}
    addr = 0
    for i, line in enumerate(lines):
        clean = line.strip()
        if not clean or clean.startswith(";"): continue
        if ":" in clean:
            label, instr = clean.split(":", 1)
            labels[label.strip()] = addr
            if instr.strip():
                parts = instr.strip().replace(",", "").split()
                addr += 1 + len(parts[1:])
        else:
            parts = clean.replace(",", "").split()
            addr += 1 + len(parts[1:])
    addr = 0
    for i, line in enumerate(lines):
        clean = line.strip()
        if not clean or clean.startswith(";"): continue
        if ":" in clean:
            parts = clean.split(":")[1].strip().replace(",", "").split()
        else:
            parts = clean.replace(",", "").split()
        if not parts: continue
        instr = parts[0].upper()
        args = parts[1:]
        instr_map[addr] = i + 1
        bytecode.append(opcode[instr])
        for arg in args:
            if arg in registers:
                bytecode.append(ord(arg))
            elif arg in labels:
                bytecode.append(labels[arg])
            elif arg.isdigit():
                bytecode.append(int(arg))
            else:
                raise Exception(f"Unknown argument: {arg}")
        addr += 1 + len(args)
    return bytecode

def compile_basic():
    basic_code = basic_editor.get("1.0", tk.END)
    try:
        asm = compile_basic_to_asm(basic_code)
        asm_editor.delete("1.0", tk.END)
        asm_editor.insert(tk.END, asm)
    except Exception as e:
        asm_editor.insert(tk.END, f"\n; Error: {e}")

def load_program(prog, offset=0):
    for i, val in enumerate(prog):
        memory[offset + i] = val

def compile_and_load():
    global pc, running
    source = asm_editor.get("1.0", tk.END)
    try:
        prog = compile_asm(source)
        pc = 0
        running = True
        for k in registers: registers[k] = 0
        for i in range(256): memory[i] = 0
        output_box.delete("1.0", tk.END)
        load_program(prog)
        update_gui()
    except Exception as e:
        print("Compile error:", e)

def compile_basic_to_asm(basic_code: str) -> str:
    lines = [l.strip() for l in basic_code.strip().splitlines()]
    label_map = {}
    asm_lines = []
    for line in lines:
        if line and line[0].isdigit():
            lineno = line.split()[0]
            label_map[lineno] = f"L{lineno}"
    for line in lines:
        if not line or not line[0].isdigit(): continue
        parts = line.split()
        lineno = parts[0]
        cmd = parts[1].upper()
        if cmd == "LET":
            var, _, val = parts[2], parts[3], parts[4]
            asm_lines.append(f"{label_map[lineno]}: MOV {var.upper()}, {val}")
        elif cmd == "DEC":
            asm_lines.append(f"{label_map[lineno]}: DEC {parts[2].upper()}")
        elif cmd == "INC":
            asm_lines.append(f"{label_map[lineno]}: INC {parts[2].upper()}")
        elif cmd == "ADD":
            asm_lines.append(f"{label_map[lineno]}: ADD {parts[2].upper()}, {parts[3].upper()}")
        elif cmd == "SUB":
            asm_lines.append(f"{label_map[lineno]}: SUB {parts[2].upper()}, {parts[3].upper()}")
        elif cmd == "IF":
            var, cond, val = parts[2], parts[3], parts[4]
            target = parts[-1]
            if cond == "!=" and val == "0":
                asm_lines.append(f"{label_map[lineno]}: JNZ {var.upper()}, {label_map[target]}")
        elif cmd == "PRINT":
            asm_lines.append(f"{label_map[lineno]}: PRINT {parts[2].upper()}")
        elif cmd == "END":
            asm_lines.append(f"{label_map[lineno]}: HLT")
    return "\n".join(asm_lines)

# GUI
root = tk.Tk()
root.title("Mini BASIC → ASM → VM")
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=10)

editor_frame = tk.Frame(left_frame)
editor_frame.pack(fill="both", expand=True)

basic_editor = tk.Text(editor_frame, height=8, width=60, bg="#eef")
basic_editor.insert(tk.END, """10 LET A = 3
20 LET C = 0
30 DEC A
40 ADD C, A
50 IF A != 0 THEN 30
60 PRINT C
70 END""")
basic_editor.pack(fill="both", expand=True)

asm_editor = tk.Text(editor_frame, height=12, width=60)
asm_editor.tag_config("highlight", background="lightblue")
asm_editor.pack(fill="both", expand=True)

btn_frame = tk.Frame(left_frame)
btn_frame.pack()
tk.Button(btn_frame, text="Step", command=step).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Compile ASM", command=compile_and_load).pack(side=tk.LEFT)
tk.Button(btn_frame, text="ASM From BASIC", command=compile_basic).pack(side=tk.LEFT)

reg_frame = tk.Frame(left_frame)
reg_frame.pack()
reg_labels = {}
for r in registers:
    tk.Label(reg_frame, text=f"{r}:").pack(side=tk.LEFT)
    reg_labels[r] = tk.Label(reg_frame, text="00000000", width=10)
    reg_labels[r].pack(side=tk.LEFT)

pc_label = tk.Label(left_frame, text="PC: 000")
pc_label.pack()
flag_label = tk.Label(left_frame, text="Z: 0")
flag_label.pack()
opcode_label = tk.Label(left_frame, text="OP: -")
opcode_label.pack()

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill="both")

mem_outer = tk.Frame(right_frame)
mem_outer.pack()

prog_mem_frame = tk.Frame(mem_outer)
prog_mem_frame.pack(side=tk.LEFT, padx=5)
tk.Label(prog_mem_frame, text="Programmspeicher (Hex)").pack()
prog_labels = []
for i in range(32):
    lbl = tk.Label(prog_mem_frame, text="000 (0x00): 00", width=20, anchor="w", bg="white")
    lbl.pack()
    prog_labels.append(lbl)

bit_mem_frame = tk.Frame(mem_outer)
bit_mem_frame.pack(side=tk.LEFT, padx=5)
tk.Label(bit_mem_frame, text="Speicher (bit)", font=("monospace", 10, "bold")).grid(row=0, column=0, columnspan=2)
mem_labels = []
for i in range(32):
    addr = tk.Label(bit_mem_frame, text=f"{i:03} (0x{i:02X})", width=10, anchor="w")
    val = tk.Label(bit_mem_frame, text="00000000", width=10, anchor="w", bg="white")
    addr.grid(row=i+1, column=0)
    val.grid(row=i+1, column=1)
    mem_labels.append((addr, val))

output_label = tk.Label(right_frame, text="Ausgabe:")
output_label.pack(anchor="w")
output_box = tk.Text(right_frame, height=4, width=30, bg="#eef")
output_box.pack()

update_gui()
root.mainloop()