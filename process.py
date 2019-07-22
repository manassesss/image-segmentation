from skimage import color, segmentation, exposure, io, filters, draw
import matplotlib.pyplot as plt 
import pydicom
import os
import numpy as np
from hunsfield import get_pixels_hu
import copy
import random

def load_FilesDicom (path) :
    """
    load all the dicom imagens in a folder
    
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

def show(im):
    """
    display an slice

    :parameter im: the slice to display
    :return:
    """
    plt.imshow(im, cmap='bone')
    plt.show()


#getting the paths of all the repositorys (volumes) with dicom images
path = "C:/Users/Manassés/Documents/Ciencia_da_Computacao/Pesquisa/LCTSC/Train"
dirs = load_PathDirs(path)

#getting an volume randomly and loading all of the images (slices) inside it
volume = copy.copy(random.choice(dirs))
print(volume)
dataset = load_FilesDicom(volume)

#selecting an slice randomly to use to get the standart template 
slice = copy.copy(random.choice(dataset))
slice  = get_pixels_hu(slice)

