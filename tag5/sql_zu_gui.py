from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import declarative_base, Session
import tkinter as tk
from tkinter import ttk

# DB-Setup
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine("sqlite:///example.db", echo=False)
Base.metadata.create_all(engine)

# Daten einfügen (nur beim ersten Start)
with Session(engine) as session:
    if session.query(User).count() == 0:
        session.add_all([
            User(name="Alice", age=30),
            User(name="Bob", age=25),
            User(name="Eve", age=35),
        ])
        session.commit()

# Datenabfrage mit WHERE-Bedingung
def fetch_users(min_age):
    with Session(engine) as session:
        stmt = select(User).where(User.age >= min_age)
        return session.scalars(stmt).all()

# GUI: Grid anzeigen
def show_gui(data):
    root = tk.Tk()
    root.title("User List")

    tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")

    for user in data:
        tree.insert("", tk.END, values=(user.id, user.name, user.age))

    tree.pack(fill="both", expand=True)
    root.mainloop()

# Anwendung starten
users = fetch_users(min_age=30)
show_gui(users)
