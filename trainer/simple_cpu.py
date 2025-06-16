import tkinter as tk
from tkinter import filedialog
import re

memory = [0] * 256
registers = {"A": 0, "B": 0, "C": 0, "D": 0}
flags = {"Z": 0}
pc = 0
running = True
instr_map = {}     # addr → editor line
active_regs = []
active_mem = []

opcode = {
    "MOV": 1,
    "ADD": 2,
    "JMP": 3,
    "HLT": 4,
    "SUB": 5,
    "INC": 6,
    "DEC": 7,
    "JNZ": 8
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
    if instr == 1:  # MOV reg, val
        reg = chr(fetch())
        val = fetch()
        registers[reg] = val
        active_regs.append(reg)
        flags["Z"] = int(registers[reg] == 0)
    elif instr == 2:  # ADD reg1, reg2
        r1 = chr(fetch())
        r2 = chr(fetch())
        registers[r1] = (registers[r1] + registers[r2]) & 0xFF
        active_regs.extend([r1, r2])
        flags["Z"] = int(registers[r1] == 0)
    elif instr == 3:  # JMP addr
        addr = fetch()
        pc = addr
    elif instr == 4:  # HLT
        running = False
    elif instr == 5:  # SUB reg1, reg2
        r1 = chr(fetch())
        r2 = chr(fetch())
        registers[r1] = (registers[r1] - registers[r2]) & 0xFF
        active_regs.extend([r1, r2])
        flags["Z"] = int(registers[r1] == 0)
    elif instr == 6:  # INC reg
        r = chr(fetch())
        registers[r] = (registers[r] + 1) & 0xFF
        active_regs.append(r)
        flags["Z"] = int(registers[r] == 0)
    elif instr == 7:  # DEC reg
        r = chr(fetch())
        registers[r] = (registers[r] - 1) & 0xFF
        active_regs.append(r)
        flags["Z"] = int(registers[r] == 0)
    elif instr == 8:  # JNZ addr
        addr = fetch()
        if flags["Z"] == 0:
            pc = addr

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
        mem_labels[i].config(text=bitstr(memory[i]), bg=bg)
        prog_labels[i].config(text=f"{i:03} (0x{i:02X}): {memory[i]:02X}", bg=bg)
    active_mem.clear()
    pc_label.config(text=f"PC: {pc:03}")
    flag_label.config(text=f"Z: {flags['Z']}")
    if current_instr is not None:
        opcode_label.config(text=f"OP: {memory[current_instr]:02X}")
    else:
        opcode_label.config(text="OP: -")
    asm_editor.tag_remove("highlight", "1.0", tk.END)
    if current_instr in instr_map:
        lineno = instr_map[current_instr]
        asm_editor.tag_add("highlight", f"{lineno}.0", f"{lineno}.end")

def load_program(prog, offset=0):
    for i, val in enumerate(prog):
        memory[offset + i] = val

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
            labels[clean.replace(":", "")] = addr
        else:
            parts = clean.replace(",", "").split()
            instr = parts[0].upper()
            addr += 1 + len(parts[1:])
    addr = 0
    for i, line in enumerate(lines):
        clean = line.strip()
        if not clean or clean.startswith(";"): continue
        if ":" in clean: continue
        parts = clean.replace(",", "").split()
        instr = parts[0].upper()
        args = parts[1:]
        instr_map[addr] = i + 1
        bytecode.append(opcode[instr])
        for arg in args:
            if re.match(r"^[-+]?\\d+$", arg):
                val = addr + int(arg)
                bytecode.append(val)
            elif arg.isalpha() and len(arg) == 1:
                bytecode.append(ord(arg))
            elif arg.isdigit():
                bytecode.append(int(arg))
            elif arg in labels:
                bytecode.append(labels[arg])
            else:
                raise Exception(f"Unknown argument: {arg}")
        addr += 1 + len(args)
    return bytecode

def compile_and_load():
    global pc, running
    source = asm_editor.get("1.0", tk.END)
    try:
        prog = compile_asm(source)
        pc = 0
        running = True
        for k in registers: registers[k] = 0
        for i in range(256): memory[i] = 0
        load_program(prog)
        update_gui()
    except Exception as e:
        print("Compile error:", e)

def load_asm_file():
    filename = filedialog.askopenfilename(filetypes=[("ASM files", "*.asm")])
    if filename:
        with open(filename) as f:
            asm_editor.delete("1.0", tk.END)
            asm_editor.insert(tk.END, f.read())

def save_asm_file():
    filename = filedialog.asksaveasfilename(defaultextension=".asm", filetypes=[("ASM files", "*.asm")])
    if filename:
        with open(filename, "w") as f:
            f.write(asm_editor.get("1.0", tk.END))

root = tk.Tk()
root.title("Mini 8-Bit CPU (ASM + Speicher + Anzeige)")
main_frame = tk.Frame(root)
main_frame.pack()

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, padx=10)

reg_frame = tk.Frame(left_frame)
reg_labels = {}
for r in registers:
    tk.Label(reg_frame, text=f"{r}:").pack(side=tk.LEFT)
    reg_labels[r] = tk.Label(reg_frame, text="00000000", width=10)
    reg_labels[r].pack(side=tk.LEFT)
reg_frame.pack()

mem_frame = tk.Frame(left_frame)
tk.Label(mem_frame, text="Speicher (bit)", font=("monospace", 10, "bold")).grid(row=0, column=0, columnspan=2)
mem_labels = []
for i in range(32):
    addr = tk.Label(mem_frame, text=f"{i:03} (0x{i:02X})", width=10, anchor="w")
    addr.grid(row=i+1, column=0)
    val = tk.Label(mem_frame, text="00000000", width=10, anchor="w", bg="white")
    val.grid(row=i+1, column=1)
    mem_labels.append(val)
mem_frame.pack()

pc_label = tk.Label(left_frame, text="PC: 000")
pc_label.pack()
flag_label = tk.Label(left_frame, text="Z: 0")
flag_label.pack()
opcode_label = tk.Label(left_frame, text="OP: -")
opcode_label.pack()

btn_frame = tk.Frame(left_frame)
tk.Button(btn_frame, text="Step", command=step).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Compile + Load", command=compile_and_load).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Load ASM", command=load_asm_file).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Save ASM", command=save_asm_file).pack(side=tk.LEFT)
btn_frame.pack()

asm_editor = tk.Text(left_frame, height=12, width=60)
asm_editor.tag_config("highlight", background="lightblue")
asm_editor.pack()

right_frame = tk.Frame(main_frame)
tk.Label(right_frame, text="Programmspeicher (Hex)").pack()
prog_labels = []
for i in range(32):
    lbl = tk.Label(right_frame, text="000 (0x00): 00", width=20, anchor="w", bg="white")
    lbl.pack()
    prog_labels.append(lbl)

asm_editor.insert(tk.END, """\
MOV A, 3
loop:
DEC A
ADD C, A
JNZ loop
HLT
""")

update_gui()
root.mainloop()
