from skimage import color, segmentation, exposure, io, filters, draw
import matplotlib.pyplot as plt 
import pydicom
import os
import numpy as np
from hunsfield import get_pixels_hu

'''

'''
def readFiles () :
    filesDicom = []
    direct = 'C:/Users/Manassés/Documents/Ciencia_da_Computacao/Pesquisa/lab_ct_1'
    for root, dirs, files in os.walk (direct, topdown=True):
        for file in files:
            filesDicom.append(pydicom.dcmread(root+"/"+file))
    
    return filesDicom

#getting all the imagens inside the repositorty 
dataset = readFiles()

plt.imshow(dataset[300].pixel_array, cmap='bone')
plt.show()

