import tkinter as tk

A = 0b00001100  # 12
B = 0b00000101  # 5

class AddGateDemo:
    def __init__(self, root):
        self.root = root
        root.title("ADD A, B auf Gatter-Ebene")
        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.pack()
        self.draw_bits()

    def draw_bits(self):
        carry = 0
        result = []
        for i in range(8):
            a_bit = (A >> i) & 1
            b_bit = (B >> i) & 1
            s = a_bit ^ b_bit ^ carry
            c_out = (a_bit & b_bit) | ((a_bit ^ b_bit) & carry)
            result.append(s)
            x = 50 + i * 60
            self.canvas.create_text(x, 20, text=str(a_bit), font=("Courier", 16))
            self.canvas.create_text(x, 50, text=str(b_bit), font=("Courier", 16))
            self.canvas.create_text(x, 80, text=str(s), font=("Courier", 16), fill="blue")
            self.canvas.create_text(x, 110, text=str(carry), font=("Courier", 12), fill="gray")
            carry = c_out
        self.canvas.create_text(480, 150, text=f"Ergebnis: {sum([bit<<i for i,bit in enumerate(result)])} (dez)", font=("Courier", 14), fill="black")
        self.canvas.create_text(480, 180, text=f"Carry-Out: {carry}", font=("Courier", 14), fill="gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = AddGateDemo(root)
    root.mainloop()