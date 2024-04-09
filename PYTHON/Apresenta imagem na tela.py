import cv2 

import numpy as np 

imgBGR = cv2.imread('lena.jpg') 

imgRGB = cv2.imread('lena.jpg') 

img_concate_Hori = np.concatenate((imgRGB, imgRGB), axis=1) 

cv2.imshow('concatenated_Hori', img_concate_Hori) 

#cv2.imshow('concatenated_Verti', img_concate_Verti) 

cv2.waitKey(0) 

cv2.destroyAllWindows()