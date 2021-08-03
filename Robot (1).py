#Proyecto Final
#Nombre: Milagros Natalie Sante Huaynates
#Código: 73610573

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

'''
    Direcciones:
        Norte [ 0 , 1]
        Oeste [-1 , 0]
        Sur   [ 0 ,-1]
        Este  [ 1 , 0]
'''

direcciones = {'Norte':[0,1], 'Oeste':[-1,0], 'Sur':[0,-1], 'Este':[1,0]}
llaves = list(direcciones.keys())

def direccion(vector):
    if vector == [ 0, 1]:
        return 'Norte'
    elif vector == [ -1, 0]:
        return 'Oeste'
    elif vector == [ 0, -1]:
        return 'Sur'
    elif vector == [ 1, 0]:
            return 'Este'

class Robot:
    def __init__(self, dir = [0,0], pos:tuple =(0,0)):
        self.dir = dir
        self.pos = list(pos)

    def fijar_dir(self, dir):
        self.dir = dir

    def fijar_pos_x(self, pos):
        self.pos[0] = pos

    def fijar_pos_y(self,pos):
        self.pos[1] = pos

    def instruccion(self, inst):
        if inst == "L":
            self.dir =  [- self.dir[1], self.dir[0]]
        elif inst == "R":
            self.dir =  [ self.dir[1], -self.dir[0]]
        elif inst == "A":
            self.pos = [self.pos[0] + self.dir[0], self.pos[1] + self.dir[1]]

    def direccion(self):
        if self.dir == [ 0, 1]:
            return 'Norte'
        elif self.dir == [ -1, 0]:
            return 'Oeste'
        elif self.dir == [ 0, -1]:
            return 'Sur'
        elif self.dir == [ 1, 0]:
            return 'Este'

    def posicion(self):
        return tuple(self.pos)

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Robot móvil")
        cw = 300 # canvas width
        ch = 250 # canvas height
        canvas = tk.Canvas(self, width=cw, height=ch, background="white")
        canvas.grid(row=3, column=0,columnspan=5)
        cycle_period = 100 # Milisegundos

        # Creamos los objetos que serán utilizados:
        rober = Robot()
        insts = ''
        def procesar():
            rober.fijar_pos_x(int(ent_x.get()) )
            rober.fijar_pos_y(int(ent_y.get()) )
            i = com_ori.current()
            rober.fijar_dir(direcciones[llaves[i]])
            insts = ent_ins.get()

            for i in range(len(insts)):
                canvas.delete(tk.ALL)
                rober.instruccion(insts[i])
                posx, posy = rober.posicion()
                dir = rober.direccion()
                print(posx, posy, dir)

                posx *= 10
                posy *= 10
                
                # Parámetros del Robot:
                ball_width = 25 # size of ball - width (x-dimension)
                ball_height = 25 # size of ball - height (y-dimension)
                color = "violet" # color of the ball
                canvas.create_oval(posx, posy, posx+ ball_width, posy + ball_height, fill=color, tag = "oval")
                canvas.update()
                canvas.after(cycle_period)
                if i + 1 != len(insts):
                    canvas.delete(tk.ALL)

            s = f"Nos encontramos en la posición {rober.posicion()} y con dirección {rober.direccion()}"
            tk.messagebox.showinfo(message = s, title="Listo!")

        # Elemento de columna 0
        txt_pos = tk.Label(self, text= "Posición\ninicial:")

        # Elementos de columna 1
        txt_x = tk.Label(self, text= "X:")
        txt_y = tk.Label(self, text= "Y:")
        
        # Elementos de columna 2
        ent_x = tk.Entry(self)
        ent_y = tk.Entry(self)

        # Elementos de columna 3
        txt_ori = tk.Label(self, text="Orientación:")
        txt_ins = tk.Label(self, text="Instrucciones")

        # Elementos de la columna 4
        com_ori = ttk.Combobox(self)
        com_ori['values'] = llaves
        ent_ins = tk.Entry(self)

        # Boton
        start = tk.Button(self, text='Iniciar',command=procesar)
        start.grid(row=2,column=1,columnspan=3)

        # Posicionamos
        # Columna 0
        txt_pos.grid(row=0, column=0, rowspan = 2)
        
        # Columna 1
        txt_x.grid(row=0,column=1)
        txt_y.grid(row=1,column=1)
        
        # Columna 2
        ent_x.grid(row=0,column=2)
        ent_y.grid(row=1,column=2)

        # Columna 3
        txt_ori.grid(row=0,column=3)
        txt_ins.grid(row=1,column=3)

        # Columna 4
        com_ori.grid(row=0,column=4)
        ent_ins.grid(row=1,column=4)


        

        '''
        
        '''
        self.mainloop()

aplicacion1=Aplicacion()
