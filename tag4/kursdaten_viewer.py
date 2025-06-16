import tkinter as tk
from tkinter import ttk
import pandas as pd
import sqlite3

DB_FILE = "kursdaten.db"
TABLE_NAME = "AAPL"

def load_data():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()
    return df

def show_data(df):
    root = tk.Tk()
    root.title(f"{TABLE_NAME} Kursdaten")

    tree = ttk.Treeview(root)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(expand=True, fill="both")
    root.mainloop()

df = load_data()
show_data(df)
