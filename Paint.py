import tkinter as tk
from Tooltip import Tooltip
from tkinter import colorchooser, filedialog, simpledialog
from PIL import Image, ImageTk, ImageGrab
from Botones import*


class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Software de Dibujo")
        self.current_tool = "pencil"
        self.current_color = "black"
        self.current_thickness = 10
        self.old_x = None
        self.old_y = None
        self.start_x = None
        self.start_y = None
        
        self.image = None

        self.listaDES = []
        self.listaRE = []

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.place(x=200, y=0, width=800, height=600)

        self.create_buttons()
        self.create_color_picker()
        self.create_thickness_slider()
        self.create_menu()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.start_paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        



    def use_pencil(self):
        self.current_tool = "pencil"

    def use_line(self):
        self.current_tool = "line"

    def use_rectangle(self):
        self.current_tool = "rectangle"

    def use_oval(self):
        self.current_tool = "oval"

    def use_text(self):
        self.current_tool = "text"

    def use_eraser(self):
        self.current_tool = "eraser"

    def choose_color(self):
        self.current_color = colorchooser.askcolor(color=self.current_color)[1]

    def create_buttons(self):
        botones = Botones(self.root, self.use_pencil, self.use_line, self.use_rectangle,
                          self.use_oval, self.use_text, self.use_eraser, self.deshacer,
                          self.rehacer)
        botones.create_tool_buttons()

    def create_color_picker(self):
        iconos = load_icons()
        self.color_btn = tk.Button(self.root, image=iconos["color"], command=self.choose_color)
        self.color_btn.image = iconos["color"]
        self.color_btn.place(x=10, y=410, width=50, height=50)
        Tooltip(self.color_btn, "presione para definir un color/ Alt + X")
        self.root.bind_all("<Alt-x>", lambda event: self.choose_color())

    def create_thickness_slider(self):
        self.thickness_slider = tk.Scale(self.root, from_=100, to=0, orient=tk.VERTICAL, label="Grosor")
        self.thickness_slider.set(self.current_thickness)
        self.thickness_slider.place(x=70, y=70, height=300)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Importar imagen", command=self.import_image)
        file_menu.add_command(label="Guardar", command=self.save_image)
        file_menu.add_command(label="Cargar", command=self.load_image)
        file_menu.add_command(label="Salir", command=self.root.quit)
        

    def start_paint(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.old_x = event.x
        self.old_y = event.y
        if self.current_tool == "text":
            self.add_text(event)

    def paint(self, event):
        self.current_thickness = self.thickness_slider.get()
        if self.old_x and self.old_y:
            if self.current_tool == "pencil":
                line = self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                               width=self.current_thickness, fill=self.current_color,
                                               capstyle=tk.ROUND, smooth=tk.TRUE)
                self.listaDES.append(line)
            elif self.current_tool == "eraser":
                line = self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                               width=self.current_thickness, fill="white",
                                               capstyle=tk.ROUND, smooth=tk.TRUE)
                self.listaDES.append(line)
            elif self.current_tool == "line":
                self.canvas.delete("temp_line")
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                        width=self.current_thickness, fill=self.current_color,
                                        capstyle=tk.ROUND, smooth=tk.TRUE, tags="temp_line")
            elif self.current_tool == "rectangle":
                self.canvas.delete("temp_shape")
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                             outline=self.current_color, width=self.current_thickness,
                                             tags="temp_shape")
            elif self.current_tool == "oval":
                self.canvas.delete("temp_shape")
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                        outline=self.current_color, width=self.current_thickness,
                                        tags="temp_shape")
            elif self.current_tool == "text":
                text = simpledialog.askstring("Entrada de texto", "Ingrese el texto a agregar:")
                self.canvas.create_text(event.x, event.y, text=text, fill=self.current_color,
                                            font=("Arial", self.current_thickness), tags="text")
                self.listaDES.append("text")

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        if self.current_tool in ["line", "rectangle", "oval"]:
            self.current_thickness = self.thickness_slider.get()
            if self.current_tool == "line":
                line = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y,
                                               width=self.current_thickness, fill=self.current_color)
                self.listaDES.append(line)
            elif self.current_tool == "rectangle":
                rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                                    outline=self.current_color, width=self.current_thickness)
                self.listaDES.append(rect)
            elif self.current_tool == "oval":
                oval = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                               outline=self.current_color, width=self.current_thickness)
                self.listaDES.append(oval)
            self.canvas.delete("temp_line")
            self.canvas.delete("temp_shape")
        self.old_x = None
        self.old_y = None
        self.start_x = None
        self.start_y = None
        self.listaRE.clear()
    
    def deshacer(self):
        if self.listaDES:
            obj = self.listaDES.pop()
            self.canvas.itemconfig(obj, state='hidden')
            self.listaRE.append(obj)

    def rehacer(self):
        if self.listaRE:
            obj = self.listaRE.pop()
            self.canvas.itemconfig(obj, state='normal')
            self.listaDES.append(obj)

    def import_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((800, 600), Image.Resampling.LANCZOS)
            self.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)


    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((800, 600), Image.Resampling.LANCZOS)
            self.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    






