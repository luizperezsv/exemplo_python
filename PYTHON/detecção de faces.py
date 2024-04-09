# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:57:19 2023

@author: Romero
"""

###############Deteccao de Faces##############
import numpy as np
import cv2
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (224, 224)

face_cascade = cv2.CascadeClassifier('vaso.jpg')

img = cv2.imread('foto vaso.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)

cont = 0
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    cont=cont + 1

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()