#########Leitura de Imagens##########
%matplotlib inline  
import cv2
import numpy as np
from IPython.display import Image
import matplotlib.pyplot as plt
import matplotlib
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

# Leitura da Imagem
img = cv2.imread('steven tyler.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

