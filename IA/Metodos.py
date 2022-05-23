from cProfile import label
import cv2
import os
from cv2 import grabCut
import imutils
import numpy as np
from ctypes import windll
from tkinter import *
from tkinter import messagebox as MessageBox

def Captura(pnombre):
    dataPath = './fotografias'

    if not os.path.exists(dataPath):
        os.makedirs(dataPath)

    pPath = dataPath + '/' + pnombre
    if not os.path.exists(pPath):
        os.makedirs(pPath)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    count = 0
    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame = imutils.resize(frame, width = 640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y: y+h, x: x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(pPath + '/rostro_{}.jpg'.format(count),rostro)
            count = count + 1

        if count >= 101:
            break

    cap.release()
    cv2.destroyAllWindows()

def Entrenador():
    dataPath = './fotografias'
    peopleList = os.listdir(dataPath)

    labels = []
    faceData = []
    label = 0

    if peopleList == []:
        from os import remove
        remove('modeloEigenFace.xml')
        return

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        for fileName in os.listdir(personPath):
            labels.append(label)
            faceData.append(cv2.imread(personPath + '/' + fileName, 0))
        label = label + 1
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.train(faceData, np.array(labels))
    face_recognizer.write('modeloEigenFace.xml')

def Reconocer():
    dataPath = './fotografias'
    peopleList = os.listdir(dataPath)

    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read('modeloEigenFace.xml')
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    teveoC = False
    Persona = 'Desconocido'

    tiempo = 0
    tiempo_max = 150

    tiempoD = 0
    tiempo_maxD = 50

    while True:
        ret, frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray, 1.3,5)

        if len(faces) == 0:
            teveoC = False
            tiempo = tiempo + 1
            if tiempo >= tiempo_max:
                user32=windll.LoadLibrary('user32.dll')
                user32.LockWorkStation()
                break
            else:
                print('No hay cara')
        
        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            ...

            if result[1] < 5700: 
                cv2.putText(frame,'{}'.format(peopleList[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y) ,(x+w, y+h), (0,0,255), 2)

                TeveoC = True
                Persona = peopleList[result[0]]
                tiempoD = 0
            else:
                cv2.putText(frame,'Desconocido', (x, y-20), 2,0.8,(0,0,255), 1, cv2.LINE_AA)
                #v2.rectangle(frame, (x,y) ,(x+w, y+h), (0,0,255), 2)

                TeveoC = False
                Persona = 'Desconocido'
                tiempoD+=1
            #print('Tiempo desconocido: ', tiempo)
            if tiempoD < tiempo_maxD:
                break
        #cv2.imshow('Video', frame)
        print("Te veo: ", Persona)
        print("Tiempo desconocido: ", tiempoD)
