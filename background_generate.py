import ctypes
from random import choice
from os import listdir
path = 'C:\\Users\\User\\OneDrive\\Desktop\\backgrounds\\'

image = choice(listdir(path))
#image = listdir(path)[-1]

ctypes.windll.user32.SystemParametersInfoW(20, 0, path + image, 3)
#print(backgroung_number)
print(listdir(path))