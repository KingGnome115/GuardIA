from multiprocessing.connection import wait
from tkinter import *
from io import open
import Metodos
import json 

class Usuario:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def leer_json():
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarios = json.load(archivo)
            return usuarios
    except:
        return []

usuarios = leer_json()

raiz = Tk()
raiz.title("GuardIA Eliminar Usuario")
raiz.resizable(0,0)
raiz.iconbitmap("./Iconos/icono.ico")

miFrame = Frame(raiz, width = 500, height = 200)
miFrame.config(bg="#0E4D40")
miFrame.pack()

etiquetaNombre = Label(miFrame, text="Nombre: ", bg="#0E4D40", fg="white")
etiquetaNombre.place(x=30, y=20)

etiquetaContrasena = Label(miFrame, text="Contraseña: ", bg="#0E4D40", fg="white")
etiquetaContrasena.place(x=200, y=20)

etiquetaEliminar = Label(miFrame, text="Eliminar: ", bg="#0E4D40", fg="white")
etiquetaEliminar.place(x=350, y=20)

cuadrosNombres = []
cuadrosContra = []
botonesEli = []

for usuario in usuarios:
    cuadroNombre1 = Label(miFrame, text=usuario['nombre'], bg="#0E4D40", fg="white")
    cuadrosNombres.append(cuadroNombre1)

    cuadroContrasena1 = Entry(miFrame, width=20)
    cuadroContrasena1.config(show="*")
    cuadrosContra.append(cuadroContrasena1)

    botonEliminar1 = Button(miFrame, text="Eliminar", width=10, height=1, bg="#0E4D40", fg="white",)
    botonesEli.append(botonEliminar1)

yy = 25
for cuadrosN in cuadrosNombres:
    cuadrosN.place(x=35, y = yy +25)
    yy+=25

yy = 25
for cuadrosC in cuadrosContra:
    cuadrosC.place(x=200, y = yy +25)
    yy+=25

yy = 15
for boton in botonesEli:
    boton.place(x=350, y = yy +30)
    yy+=30

raiz.mainloop()