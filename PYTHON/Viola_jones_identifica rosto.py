import numpy as np 

import cv2 

from matplotlib import pyplot as plt 

plt.rcParams['figure.figsize'] = (224, 224) 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 

img = cv2.imread('steven tyler.jpg') 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

faces = face_cascade.detectMultiScale(gray, 1.3, 5)  

cont = 0 

for (x,y,w,h) in faces: 

    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 

    roi_gray = gray[y:y+h, x:x+w] 

    roi_color = img[y:y+h, x:x+w] 

    cont=cont + 1   

cv2.imshow('img',img) 

cv2.waitKey(0) 

cv2.destroyAllWindows()