from tkinter import *
import Metodos

def IniciarC():
    nombre = cuadroNombre.get()
    mensaje = "Dejame recordar tu bello rostro " + nombre
    etiquetaMensaje = Label(raiz, text=mensaje, fg="#F2F2F2", bg="#0E4D40")
    etiquetaMensaje.place(x=65, y=200)

    #Metodos.Captura(nombre.get())
    #Metodos.Entrenador()


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

botonIniciar = Button(miFrame, text="Iniciar", width=10, height=1, bg="#0E4D40", fg="white", command=IniciarC)
botonIniciar.place(x=75, y=150)

raiz.mainloop()