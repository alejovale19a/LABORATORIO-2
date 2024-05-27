import tkinter as tk

def load_icons():
    iconos = {
        "lapiz": tk.PhotoImage(file=r"icon\pencil.png"),
        "borrador": tk.PhotoImage(file=r"icon\eraser.png"),
        "linea": tk.PhotoImage(file=r"icon\line.png"),
        "rectangulo": tk.PhotoImage(file=r"icon\rectangulo.png"),
        "oval": tk.PhotoImage(file=r"icon\oval.png"),
        "text": tk.PhotoImage(file=r"icon\text.png"),
        "color": tk.PhotoImage(file=r"icon\color.png"),
        "deshacer": tk.PhotoImage(file=r"icon\deshacer.png"),
        "rehacer": tk.PhotoImage(file=r"icon\rehacer.png")
    }
    return iconos
