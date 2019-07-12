from skimage import color, segmentation, exposure, io, filters, draw
import matplotlib.pyplot as plt 
import pydicom
import os
import numpy as np
from hunsfield import get_pixels_hu
import copy

def load_FilesDicom (path) :
    """
    read all the dicom imagens in a folder
    
    :parameters path: an path that leads to the source directory of images
    :returns filesDicom: an dataset with all the dicom imagens in the source directory

    """
    filesDicom = []
    direct = path
    for root, dirs, files in os.walk (direct, topdown=True):
        for file in files:
            filesDicom.append(pydicom.dcmread(root+"/"+file))
    
    return filesDicom

def load_PathDirs(path):
    """
    save all the paths in of the directorys that contains dicom images

    :parameter path: the path that contains all of the directorys with dicom images
    :return paths: an list with all of paths of the directorys with dicom images
    """

    paths = list()
    direct = path
    for root, dirs, files in os.walk (direct, topdown=True):
        for dir in dirs:
            paths.append(root + "/" + dir)
    
    return paths

#getting the paths of all the repositorys with dicom images
path = "C:/Users/Manassés/Documents/Ciencia_da_Computacao/Pesquisa/LCTSC/Train"
dirs = load_PathDirs(path)

#getting the dicom images in the repositorys with them
print(dirs[0])
for i in dirs:
    dataset = load_FilesDicom(i)

#selecting an image from the dataset tos use as example 
current = copy.copy(dataset[300])
plt.imshow(current.pixel_array, cmap='bone')
plt.show()