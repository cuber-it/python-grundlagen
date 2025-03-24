# file_viewer.py
import tkinter as tk
from tkinter import filedialog, scrolledtext

def open_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

root = tk.Tk()
root.title("Dateibetrachter")

btn = tk.Button(root, text="Datei öffnen", command=open_file)
btn.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
text_area.pack(padx=10, pady=10)

root.mainloop()
