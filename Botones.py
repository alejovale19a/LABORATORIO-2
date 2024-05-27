import tkinter as tk
from Tooltip import Tooltip
from Iconos import load_icons


class Botones:
    def __init__(self, root, use_pencil, use_line, use_rectangle, use_oval, use_text, use_eraser,
                 deshacer, rehacer):
        self.root = root
        self.use_pencil = use_pencil
        self.use_line = use_line
        self.use_rectangle = use_rectangle
        self.use_oval = use_oval
        self.use_text = use_text
        self.use_eraser = use_eraser
        self.deshacer = deshacer
        self.rehacer = rehacer
        

    def create_tool_buttons(self):
        iconos = load_icons()
        self.pencil_btn = tk.Button(self.root, image=iconos["lapiz"], command=self.use_pencil)
        self.pencil_btn.image = iconos["lapiz"]
        self.pencil_btn.place(x=10, y=10, width=50, height=50)
        Tooltip(self.pencil_btn, "presione para usar el Lápiz/ Alt + P")
        self.root.bind_all("<Alt-p>", lambda event: self.use_pencil())

        self.line_btn = tk.Button(self.root, image=iconos["linea"], command=self.use_line)
        self.line_btn.image = iconos["linea"]
        self.line_btn.place(x=10, y=70, width=50, height=50)
        Tooltip(self.line_btn, "presione para crear una Linea / Alt + L")
        self.root.bind_all("<Alt-l>", lambda event: self.use_line())

        self.rect_btn = tk.Button(self.root, image=iconos["rectangulo"], command=self.use_rectangle)
        self.rect_btn.image = iconos["rectangulo"]
        self.rect_btn.place(x=10, y=130, width=50, height=50)
        Tooltip(self.rect_btn, "presione para crear un Rectangulo/ Alt + R")
        self.root.bind_all("<Alt-r>", lambda event: self.use_rectangle())

        self.oval_btn = tk.Button(self.root, image=iconos["oval"], command=self.use_oval)
        self.oval_btn.image = iconos["oval"]
        self.oval_btn.place(x=10, y=190, width=50, height=50)
        Tooltip(self.oval_btn, "presione para crear un Circulo/ Alt + C")
        self.root.bind_all("<Alt-c>", lambda event: self.use_oval())

        self.text_btn = tk.Button(self.root, image=iconos["text"], command=self.use_text)
        self.text_btn.image = iconos["text"]
        self.text_btn.place(x=10, y=250, width=50, height=50)
        Tooltip(self.text_btn, "presione para crear Texto")

        self.erase_btn = tk.Button(self.root, image=iconos["borrador"], command=self.use_eraser)
        self.erase_btn.image = iconos["borrador"]
        self.erase_btn.place(x=10, y=310, width=50, height=50)
        Tooltip(self.erase_btn, "presione para utilizar el Borrador/ Alt + B")
        self.root.bind_all("<Alt-b>", lambda event: self.use_eraser())


        self.deshacer_btn = tk.Button(self.root, image=iconos["deshacer"], command=self.deshacer)
        self.deshacer_btn.image = iconos["deshacer"]
        self.deshacer_btn.place(x=80, y=10, width=30, height=30)
        Tooltip(self.deshacer_btn, "presione para deshacer/ Alt + Z")
        self.root.bind_all("<Alt-z>", lambda event: self.deshacer())

        self.rehacer_btn = tk.Button(self.root, image=iconos["rehacer"], command=self.rehacer)
        self.rehacer_btn.image = iconos["rehacer"]
        self.rehacer_btn.place(x=120, y=10, width=30, height=30)
        Tooltip(self.rehacer_btn, "presione para rehacer/ Alt + Y")
        self.root.bind_all("<Alt-y>", lambda event: self.rehacer())

    
    