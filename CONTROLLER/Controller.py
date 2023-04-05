from MODEL.ProductoPlaga import *
from MODEL.ProductoFertilizante import *
from MODEL.Antibiotico import *
from MODEL.Factura import *
from MODEL.Cliente import *

class Controller():
    def __init__(self):
        self.listaFacturas = []
        self.listaClientes = {}
        self.numFactura = 0
        self.listaCompra = []
        self.valorCompra = 0
        self.efectivoRecibido = 0

    def imprimirListaCompra(self):
        for producto in self.listaCompra:
            print(producto)

    def crearAntibiotico(self, nombre, dosis, tipoAnimal, precio):
        antibiotico = Antibiotico(nombre, dosis, tipoAnimal, precio)
        self.listaCompra.append(antibiotico)
        self.valorCompra += precio

    def crearPlaguicida(self, registroICA, nombre, frecuencia, precio, periodoCarencia):
        plaguicida = ProductoPlaga(registroICA, nombre, frecuencia, precio, periodoCarencia)
        self.listaCompra.append(plaguicida)
        self.valorCompra += precio

    def crearFertilizante(self, registroICA, nombre, frecuencia, precio, fechaUltimaAplicacion):
        fertilizante = ProductoFertilizante(registroICA, nombre, frecuencia, precio, fechaUltimaAplicacion)
        self.listaCompra.append(fertilizante)
        self.valorCompra += precio

    def crearFactura(self, fechaCompra, horaCompra, listaCompra, nombreCliente, cedulaCliente):
        self.numFactura += 1
        factura = Factura(fechaCompra, horaCompra, self.numFactura, self.valorCompra, listaCompra,
                          self.efectivoRecibido)
        self.listaFacturas.append(factura)

        cliente = self.listaClientes[cedulaCliente]
        cliente.añadirFactura(factura)
        factura.asociarCliente(nombreCliente, cedulaCliente)

    def crearCliente(self, nombre, cedula):
        cliente = Cliente(nombre, cedula)
        self.listaClientes[cedula] = cliente