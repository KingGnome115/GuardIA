from multiprocessing.connection import wait
from tkinter import *
from io import open
from functools import partial
import Metodos
import json 

class Usuario:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def guardar_json(usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def leer_json():
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarios = json.load(archivo)
            return usuarios
    except:
        return []

def IniciarC(raiz, cuadroNombre, cuadroContrasena):
    nombre = cuadroNombre.get()
    constrasena = cuadroContrasena.get()
    mensaje = "Dejame recordar tu bello rostro " + nombre
    etiquetaMensaje = Label(raiz, text=mensaje, fg="#F2F2F2", bg="#0E4D40")
    etiquetaMensaje.place(x=65, y=200)

    Usua = Usuario()
    Usua.nombre = nombre
    Usua.contrasena = constrasena
    usuarios = leer_json()
    if usuarios.__len__() < 3:
        usuarios.append(Usua)
        guardar_json(usuarios)
        Metodos.Captura(nombre)
        Metodos.Entrenador()
        raiz.destroy()
    else:
        mensaje = "No soy tan fuerte para proteger a tantos :c"
        etiquetaMensaje.configure(text=mensaje)
    

#Metodo para llamar esta ventana
def AgregarU():
    raiz = Tk()
    raiz.title("GuardIA Nuevo Usuario")
    raiz.resizable(0,0)
    raiz.iconbitmap("./Iconos/icono.ico")

    miFrame = Frame(raiz, width = 350, height = 350)
    miFrame.config(bg="#0E4D40")
    miFrame.pack()

    etiquetaNombre = Label(miFrame, text="Nombre: ", bg="#0E4D40", fg="white")
    etiquetaNombre.place(x=70, y=20)

    cuadroNombre = Entry(miFrame, width=30)
    cuadroNombre.place(x=75, y=50)

    etiquetaContrasena = Label(miFrame, text="Contraseña: ", bg="#0E4D40", fg="white")
    etiquetaContrasena.place(x=70, y=80)

    cuadroContrasena = Entry(miFrame, width=30)
    cuadroContrasena.config(show="*")
    cuadroContrasena.place(x=75, y=110)

    botonIniciar = Button(miFrame, text="Iniciar", width=10, height=1, bg="#0E4D40", fg="white", command=partial(IniciarC, raiz, cuadroNombre, cuadroContrasena))
    botonIniciar.place(x=75, y=150)

    raiz.mainloop()
