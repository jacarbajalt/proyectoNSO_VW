import pandas as pd
import openpyxl as opxl

#Seleccionar archivo desde explorador de archivos
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#Seleccionar archivo
Tk().withdraw()
filename = askopenfilename()

#Leer archivo xlsm
df = pd.read_excel(filename, sheet_name='Hoja1')

#Mostrar datos
print(df)

#Extraer dato de una celda de excel y copiarlo y pegarlo en la celda nueva
df['ETA'] = df['Llegados'].apply(lambda x: x*2)

