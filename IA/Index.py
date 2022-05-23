from tkinter import *
import Metodos

#Metodos.Captura("Kevin")
#Metodos.Entrenador()
#Metodos.Reconocer()

click = False

def Recon():
    global click
    click = not click
    if click:
        raiz.title("GuardIA Observando")
        botonReco.configure(image=imagenPause, bg="#0E4D40")
    else:
        raiz.title("GuardIA")
        botonReco.configure(image=imagenPlay, bg="#0E4D40")

#Venatana Principal
raiz = Tk()
raiz.title("GuardIA")
raiz.resizable(0,0)
raiz.iconbitmap("./Iconos/icono.ico")

miFrame = Frame(raiz, width = 300, height = 100)
miFrame.config(bg="#0E4D40")
miFrame.pack()

#Boton para agregar un nuevo usuario
imagenAgregar = PhotoImage(file="./Iconos/Agregar.png")
imagenAgregar = imagenAgregar.subsample(2,2)

botonAgregar = Button(miFrame, image=imagenAgregar, width=65, height=65, bg="#0E4D40", borderwidth=0)
botonAgregar.place(x=20, y=20)

#Boton para eliminar un usuario
imagenQuitar = PhotoImage(file="./Iconos/Quitar.png")
imagenQuitar = imagenQuitar.subsample(2,2)

botonQuitar = Button(miFrame, image=imagenQuitar, width=65, height=65, bg="#0E4D40", borderwidth=0)
botonQuitar.place(x=110, y=20)

#Boton para iniciar el reconocimiento
imagenPlay = PhotoImage(file="./Iconos/Play.png")
imagenPlay = imagenPlay.subsample(2,2)

imagenPause = PhotoImage(file="./Iconos/Pause.png")
imagenPause = imagenPause.subsample(2,2)

botonReco = Button(miFrame, image=imagenPlay, width=65, height=65, bg="#0E4D40", borderwidth=0, command=Recon)
botonReco.place(x=200, y=20)


raiz.mainloop()