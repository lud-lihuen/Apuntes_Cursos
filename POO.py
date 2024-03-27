# ------------------------------
# CLASES Y OBJETOS
# ------------------------------

#Nombrar clases con PascalCase:
class NombreClase():
    propiedad1 = 'valor1'
    propiedad2 = 'valor2'
    propiedad3 = 'valor3'

#Crear objeto (instancia de una clase):
objeto1 = NombreClase()

#Acceder a propiedad (atributo) de objeto:
objeto1.propiedad1

#Averiguar si un objeto es instancia de una clase:
isinstance(objeto1, NombreClase)

# ------------------------------
# CONSTRUCTOR
# ------------------------------

#Constructor de clase (parentesis opcionales despues del nombre de clase):
class NombreClase:
    def __init__(self, atributo1, atributo2):
       self.atributo1 = atributo1
       self.atributo2 = atributo2

#Construir objeto definiendo atributos:
objeto1 = NombreClase('atributo1','atributo2')

# ------------------------------
# METODOS
# ------------------------------

#Son funciones definidas para una clase

class NombreClase:
    #Metodo constructor:
    def __init__(self, atributo1, atributo2):
       self.atributo1 = atributo1
       self.atributo2 = atributo2
    #Metodo personalizado:
    def metodo(self):
        print(f'Metodo de {self}')

#Llamar metodo:
objeto1.metodo()

# ------------------------------
# HERENCIA
# ------------------------------

#Una clase hija hereda atributos y metodos de su clase padre

class ClasePadre:
    def __init__(self, atributo1, atributo2):
       self.atributo1 = atributo1
       self.atributo2 = atributo2

#Crear clase hija:
class ClaseHija(ClasePadre):
    pass
# pass es un statement nulo para dejar algo creado y reemplazar luego

#Definir atributos heredados, y atributo nuevo:
class ClaseHija(ClasePadre):
    def __init__(self, atributo1, atributo2, atributo3):
       super().__init__(atributo1, atributo2)
       self.atributo3 = atributo3

#Herencia multiple:

class ClasePadre2:
    def __init__(self, atributoA, atributoB):
       self.atributoA = atributoA
       self.atributoB = atributoB
       
    def metodo_clase2(self):
        print(f'Metodo de {self}')

class ClaseHija(ClasePadre, ClasePadre2):
    def __init__(self, atributo1, atributo2, atributoA, atributoB, atributo_propio):
       ClasePadre.__init__(atributo1, atributo2)
       ClasePadre2.__init__(atributoA, atributoB)
       self.atributo_propio = atributo_propio
    
    def metodo_clase2(self):
        return f'{super().metodo()}'

#Averiguar si una clase es subclase de otra:
issubclass(ClaseHija,ClasePadre)

# ------------------------------
# METODO DE RESOLUCION DE ORDEN (MRO)
# ------------------------------

#Tenemos una subclase que hereda metodos y atributos de dos clases (ClaseA y ClaseB).
#A su vez, cada clase hereda metodos y atributos de dos superclases respectivamente.

class SuperclaseA():
    pass

class SuperclaseB():
    pass

class ClaseA(SuperclaseA):
    pass

class ClaseB(SuperclaseB):
    pass

class Subclase(ClaseA,ClaseB):
    pass

#Si la subclase hereda un metodo o atributo con el mismo nombre que uno de las clases y superclases,
#la prioridad de ejecución al llamar al metodo o atributo se determina por el siguiente orden:

# 1) Subclase
# 2) ClaseA
# 3) SuperclaseA
# 4) ClaseB
# 5) SuperclaseB

#El orden depende del orden en que se indicaron las clases como parametros del constructor.

#Averiguar el MRO de una clase:
NombreClase.mro()

# ------------------------------
# POLIMORFISMO
# ------------------------------

#Un mismo metodo funciona diferente para cada objeto
#(no es necesario que lo hereden de una clase superior)

class Clase1():
    def metodo(self):
        return 'Resultado1'

class Clase2():
    def metodo(self):
        return 'Resultado2'

objeto1 = Clase1()
objeto2 = Clase2()

objeto1.metodo() #Resultado1
objeto2.metodo() #Resultado2

#Como funcion:

def funcion(objeto):
    return(objeto.metodo())

funcion(objeto1) #Resultado1
funcion(objeto2) #Resultado2

# ------------------------------
# ENCAPSULAMIENTO
# ------------------------------

#Hay atributos y metodos "publicos", "protegidos" y "privados" por convencion:

class Clase:
    def __init__(self):
        self.atributo_publico = 'Valor'
        self._atributo_protegido = 'Valor'
        self.__atributo_privado = 'Valor'
    
    def metodo_publico(self):
        return 'Resultado'
    
    def _metodo_protegido(self):
        return 'Resultado'
    
    def __metodo_privado(self):
        return 'Resultado'

#Se señalizan con guiones bajos

#A los atributos y metodos privados no se puede acceder de forma normal con la notacion del punto
#Se accede mediante setters y getters

#A los atributos y metodos protegidos se puede acceder mediante el punto pero se desaconseja
#Se recomienda usar setters y getters

# ------------------------------
# GETTERS, SETTERS Y DELETERS
# ------------------------------

#Un getter permite acceder a un atributo
#Un setter permite modificar el valor de un atributo
#Un deleter permite eliminar un atributo

class Clase:
    def __init__(self):
        self.atributo = 'Valor'
    
    #Definir getter:
    def get_atributo(self):
        return self.atributo
    
    #Definir setter:
    def set_atributo(self, new_atributo):
        self.atributo = new_atributo
    
    #Definir deleter:
    def delete_atributo(self):
        del self.atributo

objeto = Clase()

#Llamar al getter:
atributo = objeto.get_atributo()
#Llamar al setter:
objeto.set_atributo('Nuevo valor')
#Llamar al deleter:
objeto.delete_atributo

# ------------------------------
# DECORADORES PARA GETTERS, SETTERS Y DELETERS
# ------------------------------

# @property convierte a los getters en propiedades no modificables
# @atributo.setter convierte a los setters en propiedades modificables
# @atributo.deleter permite eliminar la propiedad

class Clase:
    def __init__(self):
        self.atributo = 'Valor'
    
    #Getter decorado:
    @property
    def atributo(self):
        return self.atributo
    
    #Setter decorado:
    @atributo.setter
    def atributo(self, new_atributo):
        self.atributo = new_atributo
    
    #Deleter decorado:
    @atributo.deleter
    def atributo(self):
        del self.atributo

objeto = Clase()

#Llamar al getter como propiedad:
atributo = objeto.atributo
#Llamar al setter como propiedad:
objeto.atributo = 'Nuevo valor'
#Llamar al deleter como propiedad:
del objeto.atributo

# ------------------------------
# CLASES ABSTRACTAS
# ------------------------------

#Abstraccion: ocultar la complejidad de la logica interna de las funciones
#Clases abstractas: plantillas para crear otras clases, no objetos

#Crear clase abstracta:
from abc import ABC, abstractclassmethod

class ClasePlantilla(ABC):
    @abstractclassmethod
    def __init__(self, atributo):
        self.atributo = atributo
    
    @abstractclassmethod
    def metodo_abstracto(self):
        pass
    
    def metodo_generico(self):
        print(f'{self}')

#Crear clase a partir de plantilla:
class Clase(ClasePlantilla):
    def __init__(self, atributo):
        super().__init__(atributo)
    
    def metodo_abstracto(self):
        print(f'{self.atributo}')

#Llamar al metodo abstracto y al generico:
Clase.metodo_abstracto()
Clase.metodo_generico()

# ------------------------------
# METODOS ESPECIALES (DUNDER)
# ------------------------------

#Son metodos integrados para cumplir funciones especiales
#Se señalizan con doble guion bajo al inicio y al final de su nombre
#Ejemplo: __init__ (metodo constructor)

class Clase:
    #Metodo constructor:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
    
    #Metodo para mostrar objeto como string al hacer print(objeto):
    def __str__(self):
        return f'Clase(atributo1={self.atributo1}, atributo2={self.atributo2})'
    
    #Metodo para mostrar representacion del objeto al hacer eval(repr(objeto)):
    def __repr__(self):
        return f'Clase({self.atributo1}, {self.atributo2})'
    
#Muchos metodos especiales permiten sobrecarga de metodos
#Ejemplo: definir lo que pasa al sumar dos objetos de cierta clase:
# __add__(self, other)

# ------------------------------
# PRINCIPIOS SOLID
# ------------------------------

#Convenciones y buenas practicas para facilitar el mantenimiento y escalabilidad del codigo

# S - SRP: Principio de Responsabilidad Unico
# O - OCP: Principio de Abierto/Cerrado
# L - LSP: Principio de Sustitucion de Liskov
# I - ISP: Principio de Segregacion de Interfaz
# D - DIP: Principio de Inversion de Dependencias

# SINGLE RESPONSABILITY PRINCIPLE

#Cada clase tiene que tener una unica responsabilidad o funcionalidad
#Cada clase debe poder cumplir con su funcionalidad sin depender de otras

# OPEN/CLOSED PRINCIPLE

#Las entidades tienen que estar abiertas para la extension pero cerradas para la modificacion
#Se debe poder gregar funcionalidades sin tener que modificar las ya existentes

# LISKOV'S SUBSTITUTION PRINCIPLE

#Por Barbara Liskov
#Las clases derivadas deben ser sustituibles por sus clases base
#Una clase debe poder utilizarse en todos los lugares donde su subclase pueda utilizarse

# INTERFACE SEGREGATION PRINCIPLE

#Ningun cliente debe ser forzado a depender de interfaces que no utilice
#Se debe eliminar las dependencias que no se van a utilizar

# DEPENDENCY INVERSION PRINCIPLE

#Los modulos de alto nivel no deben depender de los de bajo nivel, ambos deben depender de las abstracciones
#Las abstracciones no deben depender de los detalles, sino al reves
#Es decir: las funcionalidades mas basicas no deben depender de las mas especificas, sino al reves
