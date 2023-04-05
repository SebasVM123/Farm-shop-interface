class Cliente():
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__listaFacturas = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cedula(self):
        return self.__cedula

    @property
    def listaFacturas(self):
        return self.__listaFacturas

    def añadirFactura(self, factura):
        self.__listaFacturas.append(factura)