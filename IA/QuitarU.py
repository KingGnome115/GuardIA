from multiprocessing.connection import wait
from shutil import rmtree
from tkinter import *
from io import open
from functools import partial
from os import remove
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

def guardar_json(usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def Eliminar(usuarioE, cont, raiz, cuadrosContra):
    contrasena = cuadrosContra[cont].get()
    print("La contraseña de " + usuarioE['nombre'] + " es: " + contrasena)
    if contrasena == usuarioE['contrasena']:
        usuarios = leer_json()
        usuarios.remove(usuarioE)
        rmtree('fotografias/' + usuarioE['nombre'] + '/')
        Metodos.Entrenador()
        guardar_json(usuarios)
        raiz.destroy()
    else:
        mensaje = "Contraseña Incorrecta "
        etiquetaMensaje = Label(raiz, text=mensaje, fg="#F2F2F2", bg="#0E4D40")
        etiquetaMensaje.place(x=200, y=150)

#Metodo para llamar esta ventana
def QuitarU():

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
    cont = 0

    for usuario in usuarios:
        cuadroNombre1 = Label(miFrame, text=usuario['nombre'], bg="#0E4D40", fg="white")
        cuadrosNombres.append(cuadroNombre1)

        cuadroContrasena1 = Entry(miFrame, width=20)
        cuadroContrasena1.config(show="*")
        cuadrosContra.append(cuadroContrasena1)

        botonEliminar1 = Button(miFrame, text="Eliminar", width=10, height=1, bg="#0E4D40", fg="white", command=partial(Eliminar, usuario, cont, raiz, cuadrosContra))
        botonesEli.append(botonEliminar1)
        cont += 1

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
