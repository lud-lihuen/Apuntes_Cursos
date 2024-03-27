# ------------------------------
# MODULOS
# ------------------------------

#Se puede enlazar otros archivos .py (modulos) para utilizar sus funciones:

# import nombre_archivo as nombre_modulo (el as es opcional)

#Para usar una funcion de ese modulo, se la llama como metodo del mismo:

# nombre_modulo.funcion()

#Se puede importar solo una funcion/metodo/objeto de un modulo (acepta usar as):

# from nombre_archivo import nombre_objeto

#Si el modulo se encuentra en otra carpeta del workspace:

# import nombre_carpeta.nombre_archivo

#Si el modulo se encuentra en una carpeta externa:

# import sys
# sys.path.append('ruta_carpeta')
# import nombre_archivo

# ------------------------------
# PAQUETES
# ------------------------------

#Los paquetes son carpetas con varios modulos
#Dicha carpeta debe contener un archivo en blanco con nombre __init__.py para que Python entienda que es un paquete

#Para importar un modulo de un paquete:
# import nombre_paquete.nombre_modulo

# ------------------------------
# ARCHIVOS TXT
# ------------------------------

# archivo = open('ruta_archivo', encoding='UTF-8')
# leer_archivo_completo = archivo.read()
# leer_archivo_por_lineas = archivo.readlines()
# leer_linea_n = archivo.readline(n)
# archivo.close()

#Cerrar archivo siempre despues de usarlo

#Forma alternativa que cierra archivo automaticamente luego de ejecutar instrucciones:
#Argumento 'w' habilita permisos de escritura

with open('ruta_archivo', 'w', encoding='UTF-8') as archivo:
    contenido = archivo.read()
    #Agregar una linea al archivo:
    archivo.write('Texto a escribir')
    #Para escribir varias lineas se usa un vector y el separador \n al final de cada linea:
    archivo.writelines(['Linea 1\n', 'Linea 2'])

#Con argumento 'a' en el open, el metodo write funciona como append y agrega sin sobreescribir

# ------------------------------
# ARCHIVOS CSV (Vectores Separados por Comas)
# ------------------------------

#Importar:

import csv
with open('ruta_archivo', encoding='UTF-8') as archivo:
    contenido = csv.reader(archivo)

#Con Pandas:
import pandas as pd
df = pd.read_csv('ruta_archivo', names=['columna 1', 'columna 2']) #data frame

#Operar:

n = 1
m = 2

df.describe() #muestra info del data frame

filas, columnas = df.shape() #devuelve vector con cantidad de filas y columnas del data frame

primeras_filas = df.head(n) #primeras n filas
ultimas_filas = df.tail(n) #ultimas n filas

elemento_especifico = df.loc[n, 'columna']
elemento_especifico = df.iloc[n, m]

variable1 = df['columna 1']
variable1 = df.loc[:, 'columna 1']
variable1 = df.iloc[:, 1]

df2 = df.sort_values('columna 1') #ordena el data frame segun los valores de la columna 1
#Se puede agregar el argumento ascending = False para invertir el orden

filtrado = df.loc[df['columna 1']==True, :] #se puede poner cualquier condicion tanto en filas como columnas

df = df.concat([df, df2]) #concatena data frames

# ------------------------------
# EJEMPLOS: TRABAJAR CON ARCHIVOS
# ------------------------------

# TXT

nombres = ['Juan', 'Pedro', 'Maria', 'Jose']
apellidos = ['Suarez', 'Fernandez', 'Garcia', 'Perez']

with open('registro.txt', 'w') as registro:
    registro.writelines('Personas registradas:\n')
    for i,k in zip(nombres,apellidos):
        registro.writelines(f'Nombre: {i}\nApellido: {k}\n---------\n')

# CSV

import pandas as pd
df = pd.read_csv('ruta_archivo.csv')

#Convertir a string los datos de una columna:
df['columna 1'] = df['columna 1'].astype(str)
#Reemplazar un dato en una columna:
df['columna 1'].replace('dato_viejo', 'dato_nuevo', inplace=True)

#Eliminar filas con datos faltantes:
df = df.dropna()
#Eliminar columnas con datos faltantes:
df = df.dropna(axis=1)
#Eliminar filas repetidas:
df = df.drop_duplicates()

#Guardar data frame como archivo csv:
df.to_csv('nombre_archivo.csv')

# ------------------------------
# GRAFICOS
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('ruta_archivo.csv')

#Grafico de lineas:
sns.lineplot(x='columna 1', y='columna 2', data=df)
#Marcar punto en grafico:
plt.plot('valor x', 'valor y', 'o')

#Grafico de barras:
sns.barplot(x='columna 1', y='columna 2', data=df)

#Grafico de dispersion:
sns.scatterplot(x='columna 1', y='columna 2', data=df)

#Boxplot:
sns.boxplot(x='columna 1', y='columna 2', data=df)

#Mostrar grafico:
plt.show()

# ------------------------------
# LEER ARCHIVOS MUY GRANDES
# ------------------------------

#Con pandas:
import pandas as pd

def read_csv_in_chunks(file_name):
    for i, chunk in enumerate(pd.read_csv(file_name, chunksize=1000)):
        print('Chunk #{}'.format(i))
        print(chunk)

read_csv_in_chunks('big_file.csv')

#Con csv:
import csv

def read_csv_in_chunks(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, chunk in enumerate(reader):
            print('Chunk #{}'.format(i))
            print(chunk)

read_csv_in_chunks('big_file.csv')
