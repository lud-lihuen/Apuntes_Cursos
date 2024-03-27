# ------------------------------
# VARIABLES
# ------------------------------

a = 1 #declaro y defino o redefino
a += 1 #redefino respecto al valor anterior
del a #borra variable
#Nombrar variables con snake_case en vez de camelCase (tampoco PascalCase, que se usa para clases)

# ------------------------------
# DATOS SIMPLES
# ------------------------------

string = "string en una linea"
string = 'string en una linea'

"""string
    en diferentes
    lineas"""

'''string
    en diferentes
    lineas'''

entero = 1 #int (integer)
decimal = 1.1 #float

True
False
#Booleanos se escriben con mayuscula inicial

# ------------------------------
# DATOS COMPUESTOS
# ------------------------------

lista = ['a', 1, 1.1, True]
lista[0] = 'b' #redefino primer elemento de la lista
lista[1:3] #llamo elementos desde el 1 hasta el 3 (slicing)

tupla = ('a', 1, 1.1, True) #se pueden omitir los parentesis, tupla de un solo dato lleva coma al final
print(tupla[0])
#Tupla o upla es una lista que no se puede modificar sus elementos (pero si redefinirse completa)

conjunto = {'a', 1, 1.1, True}
#Set o conjunto es una lista sin orden especifico y no permite repetir valores
#Se puede llamar completo pero no por elementos

diccionario = {
    'a' : True,
    'b' : 1,
    'c' : 'a',
    'key' : 'value',
    'clave' : 'valor'
}
diccionario['a'] = False
#No se escribe coma despues del ultimo valor del diccionario

# ------------------------------
# OPERADORES ARITMETICOS
# ------------------------------

1 + 1
1 - 1
1 * 1
1 / 1 #devuelve un dato tipo float aunque sea entera
1 ** 1 #potencia
1 // 1 #division baja: devuelve la parte entera del resultado (integer)
1 % 1 #modulo o resto de la division

# ------------------------------
# OPERADORES DE COMPARACIÓN
# ------------------------------

1 == 1
1 != 1
1 < 1
1 <= 1
1 > 1
1 >= 1

# ------------------------------
# OPERADORES DE PERTENENCIA
# ------------------------------

'a' in string #verifica si se encuentra
'a' not in string #verifica si NO se encuentra

# ------------------------------
# OPERADORES LOGICOS
# ------------------------------

True & False #False
True | False #True
not True #False

# ------------------------------
# CONDICIONALES IF
# ------------------------------

if 1 == 1:
    print(True)
elif 1 != 1:
    print(False)
else:
    print('WTF?')
#Else if se escribe elif

# ------------------------------
# BUCLES FOR
# ------------------------------

iterable = [1, 2, 3]
otro_iterable = ['a', 'b', 'c']
string = 'String'
diccionario = {
    'a' : True,
    'b' : 1,
    'c' : 'a',
    'key' : 'value',
    'clave' : 'valor'
}

for i in iterable:
    print(i)
#Itera entre elementos de un iterable

for i,k in zip(iterable, otro_iterable):
    print(i)
    print(k)
#Itera alternando entre dos iterables del mismo tamaño

for i in range(0, 10):
    print(i)
#Itera en un rango numerico, se puede usar range(n) para que itere n veces

for i in enumerate(iterable):
    indice = i[0]
    elemento = i[1]
#Itera entre tuplas (indice, elemento) a partir del iterable

for letra in string:
    print(letra)

for i in diccionario.items():
    clave = i[0]
    valor = i[1]
#Itera entre pares (clave, valor) de un diccionario

#For con excepciones:
for i in otro_iterable:
    if i == 'b':
        continue
    #Continue hace que salte a la siguiente iteracion sin ejecutar las instrucciones para esta
    if i == 'c':
        break
    #Break corta el bucle (e impide la ejecucion del else si lo hubiera)
    print(i)
else:
    print('fin de bucle')
#Else siempre se ejecuta en el for como ultima iteracion (a menos que haya un break)

#For en una sola linea de codigo:
iterable_duplicado = [i*2 for i in iterable]

# ------------------------------
# BUCLES WHILE
# ------------------------------

i = 0
while i < 10:
    print(i)
    i += 1

# ------------------------------
# OPERAR CON VARIABLES
# ------------------------------

#Concatenar strings:
nombre = 'Lihuen'
bienvenida = 'Hola ' + nombre + ', bienvenido'
bienvenida = f'Hola {nombre}, bienvenido' #f-strings

#Desempaquetar arrays:
datos = ['a','b']
a,b = datos #define a='a' y b='b'

# ------------------------------
# METODOS DE CADENA
# ------------------------------

string = 'String'

string.upper() #convierte todo a mayusculas
string.lower() #convierte todo a minusculas
string.capitalize() #pone solo la primera letra en mayusculas

string.find('i') #encuentra el indice de la primera aparicion del parametro (da -1 si no encuentra nada)
string.index('i') #igual a find pero si no encuentra nada tira error
string.count('Str') #devuelve el numero de ocurrencias del parametro

string.isnumeric() #verifica si es numerico (incluso si es un string con solo numeros)
string.isalpha() #verifica si es alfanumerico (solo numeros y letras sin espacios ni caracteres especiales)
string.startswith('S') #verifica si la cadena empieza con el parametro
string.endswith('g') #verifica si la cadena termina con el parametro

string.replace('t','p') #reemplaza el primer parametro por el segundo
string.split('i') #separa usando parametro como separador, devuelve una lista

# ------------------------------
# METODOS DE LISTAS
# ------------------------------

lista = ['a', 1, 1.1, True]

lista.append('False') #agrega un elemento al final de la lista
lista.insert(1,'b') #agrega un elemento en el indice indicado
lista.extend(['False', 'b', 2]) #agrega varios elementos al final de la lista

lista.pop(0) #elimina un elemento en el indice indicado (-1 para eliminar el ultimo, -2 el anteultimo etc)
lista.remove('a') #elimina el elemento indicado
lista.clear() #elimina todos los elementos

lista.sort() #ordena de menor a mayor
lista.sort(reverse=True) #ordena de mayor a menor
lista.reverse() #invierte el orden de los elementos

# ------------------------------
# METODOS DE CONJUNTOS
# ------------------------------

conjunto = {'a', 1, 1.1, True}
otro_conjunto = {'a', 1, 1.1, True, 'b', 2, 2.2, False}

conjunto.issubset(otro_conjunto) #verifica si es subconjunto (tambien se pueden comparar con <=)
conjunto.issuperset(otro_conjunto) #verifica si es superconjunto (tambien se pueden comparar con >)
conjunto.isdisjoint(otro_conjunto) #verifica si no hay ningun elemento en comun

# ------------------------------
# METODOS DE DICCIONARIOS
# ------------------------------

diccionario = {
    'a' : True,
    'b' : 1,
    'c' : 'a',
    'key' : 'value',
    'clave' : 'valor'
}

diccionario.keys() #devuelve una lista con las claves
diccionario.get('a') #devuelve el valor de la clave indicada, y None si no la encuentra
diccionario.clear() #elimina el contenido del diccionario
diccionario.pop('a') #elimina el elemento indicado
diccionario.items() #genera una lista iterable con los pares clave-valor del diccionario

# ------------------------------
# FUNCIONES INTEGRADAS
# ------------------------------

print(a) #imprime en consola
type(a) #muestra tipo de dato
len(a) #length
dir(a) #devuelve lista de atributos y metodos del objeto
input('Prompt') #muestra el prompt y devuelve el string que inserte el usuario

int(a) #convierte a numero
float(a) #convierte a float
str(a) #convierte a string
list(a) #crea lista a partir de vector
tuple(a) #crea tupla a partir de vector
set(a) #crea conjunto a partir de vector
frozenset(a) #crea conjunto no modificable a partir de vector
dict(clave1='valor1', clave2='valor2') #crea diccionario
dict.fromkeys(['clave1', 'clave2']) #crea diccionario con valores vacios a partir de vector de claves

max(a) #busca el maximo en un vector numerico
min(a) #busca el minimo en un vector numerico
sum(a) #suma todos los elementos de un vector numerico
round(a,2) #redondea un numero (el segundo argumento son las cifras decimales, si no se incluye será 0)

bool(a) #devuelve False si se le pasa 0, datos vacios, False o None
all(a) #igual a bool pero verifica todos los elementos de un iterable
filter(bool, iterable) #devuelve un iterable con los elementos del segundo argumento que verifican el primer argumento

# ------------------------------
# DEFINIR FUNCIONES
# ------------------------------

#Definir funcion:
def funcion(parametros):
    resultado = len(parametros)
    return resultado

#Llamar funcion:
funcion(a)

#Tomar argumentos y convertirlos en vector:
def funcion(*args):
    return sum(args)

#Funcion con parametro seteado por defecto:
def funcion(parametro = 0):
    return parametro

#Funcion con condicional y bucle:
def es_primo(numero):
    if numero == 2: return False
    for i in range(2, numero-1):
        if numero % i == 0: return False
    return True
#Si ejecuta el return del if, se corta el bucle, si no, ejecuta el ultimo return

# ------------------------------
# FUNCIONES LAMBDA
# ------------------------------

resultado = lambda a : round(a)

# ------------------------------
# DECORADORES
# ------------------------------

#Agregan funcionalidades extra a otras funciones definidas

#Definir decorador:
def decorador(funcion):
    def funcion_extra():
        print('Antes de llamar a la funcion')
        funcion()
        print('Despues de llamar a la funcion')
    return funcion_extra()

#Utilizarlo renombrando funcion:
def funcion():
    return 'Funcion'

funcion_modificada = decorador(funcion)
funcion_modificada()

#Utilizarlo sin renombrar funcion:
@decorador
def funcion():
    return 'Funcion'

funcion()

# ------------------------------
# MANEJO DE EXCEPCIONES (ERRORES)
# ------------------------------

#Sentencias que pueden ir dentro de la funcion definida:

#Instrucciones de la funcion si todo esta ok:
try:
    print('Instrucciones')
#Instrucciones para el caso de excepcion (error):
except:
    print('Error')
#Instrucciones que se ejecutan despues del try si no hay excepcion:
else:
    print('Instrucciones')
#Instrucciones que se ejecutan independientemente de si se ejecuto el try o el except:
finally:
    print('Instrucciones')

#Acceder al objeto excepcion:
try:
    print('Instrucciones')
except Exception as e:
    print(f'Error: {e}')

#Se puede crear una excepcion personalizada como objeto:
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Error: {err}')
        
#Manejar la excepcion personalizada:
try:
    print('Instrucciones')
except:
    raise MiExcepcion('Mensaje de error')

# ------------------------------
# EXPRESIONES REGULARES
# ------------------------------

#Modulo oficial de Python para trabajar con expresiones regulares:
import re

texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat.'''

#Buscar coincidencias (todas) sin expresiones regulares:
re.findall('Lorem', texto, flags=re.IGNORECASE)
#Buscar solo la primera coincidencia:
re.search('Lorem', texto)

#Expresiones regulares:
# \d - digitos numericos del (0-9)
# \w - caracteres alfanumericos (a-z, A-Z, 0-9, _)
# \s - espacios en blanco, tabulaciones y saltos de linea
# \n - salto de linea
# . - todo menos salto de linea
# ^ - comienzo de linea
# $ - fin de linea
# \ - caracteres especiales (escribir el caracter especifico despues de la \)
# * - comodin (cualquier caracter o ningun caracter)
# % - comodin (cualquier caracter, al menos uno)
# ? - indica como opcional la expresion que le antecede
# {n} - repite n veces la expresion que le antecede
# {n,m} - al menos n, maximo m
# () - agrupar caracteres para aplicar {n} a todo el conjunto
# [] - agrupar caracteres para aplicar {n} a cada caracter del grupo
# | - operador or para buscar una cosa o la otra (si estan ambas muestra las dos)

#Buscar coincidencias con expresiones regulares:
re.findall(r'\d', texto)
#Buscar TODO MENOS caracteres alfanumericos:
re.findall(r'\W', texto)

#Ejemplo: buscar palabra al comienzo de una linea:
re.findall(r'^Ut', texto, flags=re.M)
# flags=re.M activa la deteccion multi linea

#Ejemplo: buscar fecha DD/MM/AAAA:
re.search(r'\d{2}/\d{2}/\d{4}', texto)

#Ejemplo: buscar una direccion de e-mail:
re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)

#Ejemplo: buscar direccion web:
re.findall(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto)

#Reemplazar una expresion por otra:
texto = re.sub(r'expresion', 'reemplazo', texto)
#Ejemplo: reemplazar vocales por asteriscos:
texto = re.sub('[aeiou]', '*', texto)
