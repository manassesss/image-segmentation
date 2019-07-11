import numpy as np
import pydicom
import os
import matplotlib.pyplot as plt
from dicompylercore import dicomparser

def get_pixels_hu(im):
    ds = dicomparser.DicomParser(im)
    #intercept, slope = ds.GetRescaleInterceptSlope
    intercept = im.RescaleIntercept
    slope = im.RescaleSlope
    rescale = im.pixel_array * slope + intercept
    window, level = ds.GetDefaultImageWindowLevel()
    pixel = ds.GetLUTValue(rescale, window, level)
    return pixel