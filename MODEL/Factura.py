from MODEL.ProductoPlaga import *
from MODEL.ProductoFertilizante import *
from MODEL.Antibiotico import *

class Factura():
    def __init__(self, fechaCompra, horaCompra, numeroFactura, valorTotal, listaCompra, efectivoRecibido):
        self.__fechaCompra = fechaCompra
        self.__horaCompra = horaCompra
        self.__valorTotal = valorTotal
        self.__numeroFactura = numeroFactura
        self.__listaCompra = listaCompra
        self.__efectivoRecibido = efectivoRecibido
        self.cliente = {}

    @property
    def fechaCompra(self):
        return self.__fechaCompra

    @property
    def horaCompra(self):
        return self.__horaCompra

    @property
    def valorTotal(self):
        return self.__valorTotal

    @property
    def numeroFactura(self):
        return self.__numeroFactura

    @property
    def listaCompra(self):
        return self.__listaCompra

    @property
    def efectivoRecibido(self):
        return self.__efectivoRecibido

    def asociarCliente(self, nombre, cedula):
        self.cliente['Nombre'] = nombre
        self.cliente['Cedula'] = cedula