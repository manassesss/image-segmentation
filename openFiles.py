import os
import pydicom
import matplotlib.pyplot as plt

global filesDicom = []

direct = 'C:/Users/Manassés/Documents/Ciencia_da_Computacao/Pesquisa/lab_2/DICOM/S00001/SER00011'

for root, dirs, files in os.walk (direct, topdown=True):
    for file in files:
        filesDicom.append(pydicom.dcmread(root+"/"+file))

print(len(filesDicom))
fig, axes = plt.subplots(ncols=(len(filesDicom)), figsize=(10,10))
for i in range (len(filesDicom)):
        axes[i].imshow(filesDicom[i].pixel_array, cmap='bone')

plt.show()