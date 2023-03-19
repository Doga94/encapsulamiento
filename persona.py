class Persona:
    #Atributos publicos
    #nombre = None
    #edad = None
    
    #atributos privados
    __nombre = None
    __edad = None

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    #Metodo privado
    def __metodo_privado(self):
        print('Soy un metodo privado')

    def get_nombre(self):
        return self.__nombre
    
    #Modificar metodo
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    #Modificar metodo
    def set_edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}'
