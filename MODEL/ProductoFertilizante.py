from MODEL.ProductoControl import ProductoControl

class ProductoFertilizante(ProductoControl):
    def __init__(self, registroICA, nombre, frecuencia, precio, fechaUltimaAplicacion):
        super().__init__(registroICA, nombre, frecuencia, precio)
        self.__fechaUltimaAplicacion = fechaUltimaAplicacion

    @property
    def fechaUltimaAplicacion(self):
        return self.__fechaUltimaAplicacion