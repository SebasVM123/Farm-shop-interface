class Antibiotico():
    def __init__(self, nombre, dosis, tipoAnimal, precio):
        self.__nombre = nombre
        self.__dosis = dosis
        self.__tipoAnimal = tipoAnimal
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dosis(self):
        return self.__dosis

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @property
    def precio(self):
        return self.__precio