import cv2
import os
from ctypes import windll

dataPath = './fotografias'
peopleList = os.listdir(dataPath)
print('Lista de personas' , peopleList)

#Metodo de entrenamiento
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.EigenFaceRecognizer_create()

#lectura del modelo
face_recognizer.read('modeloEigenFace.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

TeveoC = False
Persona = 'Desconocido'

#Variables de tiempo para saber cuanto tiempo esta persona en desconocido
tiempo = 0
tiempo_max = 150

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    #Verificamos que veamos caras
    if len(faces) == 0:
        tiempo = tiempo + 1
        if tiempo >= tiempo_max:
            user32=windll.LoadLibrary('user32.dll')
            user32.LockWorkStation()
            break

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        print(result)
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        ...
        #fisherface
        if result[1] < 5700: 
            cv2.putText(frame,'{}'.format(peopleList[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y) ,(x+w, y+h), (0,0,255), 2)

            TeveoC = True
            Persona = peopleList[result[0]]
            tiempo = 0
        else:
            cv2.putText(frame,'Desconocido', (x, y-20), 2,0.8,(0,0,255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y) ,(x+w, y+h), (0,0,255), 2)

            TeveoC = False
            Persona = 'Desconocido'
            tiempo+=1
            #print('Tiempo desconocido: ', tiempo)
            #if tiempo < tiempo_max:
            #    break
    cv2.imshow('frame', frame)
    #print('Tiempo: ', tiempo)
    k = cv2.waitKey(1)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()