# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:58:09 2023

@author: Romero
"""

###################################Histograma de Cores####################################
##Os histogramas apresentam a intensidade de cada canal de cor presente em cada imagem####

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem com seus dados de altura, largura e canais
# Cria a tupla colors (BGR) e cria a lista features
img = cv2.imread('imagem/serie.jpg',-1)
height, width, channels = img.shape
colors = ('b', 'g', 'r')
features=[]

#Cria a máscara
mask = np.zeros(img.shape[:2], np.uint8)
mask[int(height*0.1):int(height*0.9), 0:int(width*0.6)] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)



#Exemplo Doc OpenCV
#Carrega a imagem com a adição da máscara
for i,col in enumerate(colors):
    hist_mask = cv2.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist_mask, color=col)
    plt.xlim([0, 256])
plt.show()