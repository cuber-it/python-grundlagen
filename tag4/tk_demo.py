import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename(title="Datei auswählen")
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())

def exit_app():
    root.quit()

root = tk.Tk()
root.title("File Reader mit Menü")

# Menü
menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Öffnen", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=exit_app)
menu.add_cascade(label="Datei", menu=file_menu)
root.config(menu=menu)

# Textfeld
text = tk.Text(root, wrap='word')
text.pack(expand=True, fill='both')

root.mainloop()
