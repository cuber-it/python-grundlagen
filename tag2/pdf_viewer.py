import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import fitz  # PyMuPDF

class PDFViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple PDF Viewer")

        self.canvas = tk.Label(root)
        self.canvas.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Open PDF", command=self.load_pdf).pack(side="left")
        tk.Button(btn_frame, text="<<", command=self.prev_page).pack(side="left")
        tk.Button(btn_frame, text=">>", command=self.next_page).pack(side="left")

        self.doc = None
        self.page_num = 0
        self.image = None

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.doc = fitz.open(file_path)
            self.page_num = 0
            self.show_page()

    def show_page(self):
        if not self.doc:
            return
        page = self.doc.load_page(self.page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.image = ImageTk.PhotoImage(img)
        self.canvas.config(image=self.image)

    def next_page(self):
        if self.doc and self.page_num < len(self.doc) - 1:
            self.page_num += 1
            self.show_page()

    def prev_page(self):
        if self.doc and self.page_num > 0:
            self.page_num -= 1
            self.show_page()

if __name__ == "__main__":
    root = tk.Tk()
    viewer = PDFViewer(root)
    root.mainloop()
