from MODEL.ProductoControl import ProductoControl

class ProductoPlaga(ProductoControl):
    def __init__(self, registroICA, nombre, frecuencia, precio, periodoCarencia):
        super().__init__(registroICA, nombre, frecuencia, precio)
        self.__periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self):
        return self.__periodoCarencia