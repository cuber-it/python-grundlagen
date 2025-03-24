import tkinter as tk
from tkinter import messagebox

def read_file():
    filename = entry.get()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

root = tk.Tk()
root.title("Datei anzeigen")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=(0, 5))

button = tk.Button(frame, text="Öffnen", command=read_file)
button.pack(side=tk.LEFT)

text = tk.Text(root, wrap="word", height=20, width=60)
text.pack(padx=10, pady=(0, 10))

root.mainloop()
