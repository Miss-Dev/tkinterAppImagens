import os
from tkinter import filedialog

a = filedialog.askdirectory()
pasta = a
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(os.path.realpath(diretorio), arquivo))
print(a)