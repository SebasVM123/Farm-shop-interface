class ProductoControl():
    def __init__(self, registroICA, nombre, frecuencia, precio):
        self.__registroICA = registroICA
        self.__nombre = nombre
        self.__frecuencia = frecuencia
        self.__precio = precio

    @property
    def registroICA(self):
        return self.__registroICA

    @property
    def nombre(self):
        return self.__nombre

    @property
    def frecuencia(self):
        return self.__frecuencia

    @property
    def precio(self):
        return self.__precio