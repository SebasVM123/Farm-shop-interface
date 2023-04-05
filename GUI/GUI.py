import sys
from functools import partial
from datetime import date
from datetime import datetime
from CONTROLLER.Controller import *
from PyQt5 import uic, QtWidgets,QtCore,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor

class TiendaAgricola(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Interfaz/tienda.ui', self)

        self.move(90, 20)

        with open("Interfaz/styles.css") as f:
            self.setStyleSheet(f.read())

        self.__controller = Controller()

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.pushButton1)
        self.buttonGroup.addButton(self.pushButton2)
        self.buttonGroup.addButton(self.pushButton3)
        self.buttonGroup.addButton(self.pushButton4)
        self.buttonGroup.addButton(self.pushButton5)
        self.buttonGroup.addButton(self.pushButton6)
        self.buttonGroup.addButton(self.pushButton7)
        self.buttonGroup.addButton(self.pushButton8)
        self.buttonGroup.addButton(self.pushButton9)
        self.buttonGroup.addButton(self.pushButton10)
        self.buttonGroup.addButton(self.pushButton11)
        self.buttonGroup.addButton(self.pushButton12)
        self.buttonGroup.addButton(self.pushButton13)
        self.buttonGroup.addButton(self.pushButton14)
        self.buttonGroup.addButton(self.pushButton15)
        self.buttonGroup.addButton(self.pushButton16)
        self.buttonGroup.addButton(self.pushButton17)
        self.buttonGroup.addButton(self.pushButton18)

        self.pushButtonPagar.setEnabled(False)
        self.pushButtonPagar.setStyleSheet('QPushButton{color: black; font: 12pt;}')
        self.layoutCompra = QVBoxLayout()
        self.layoutCompra.setAlignment(QtCore.Qt.AlignTop)
        self.widgetCompra = QWidget()
        self.widgetCompra.setLayout(self.layoutCompra)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widgetCompra)
        self.scrollArea.setStyleSheet('QScrollArea QLabel{font-size: 14pt;}')

        self.botonDatos = QPushButton('Ingresar')
        self.botonDatos.setStyleSheet('QPushButton{font: 12pt; border-radius: 3px}')
        self.botonDatos.setFixedHeight(26)
        self.botonDatos.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.labelCliente = QLabel()
        self.labelCliente.setStyleSheet('QLabel{font: 14pt;}')
        self.labelCliente.setFixedHeight(40)
        self.lineEditCedula.setEnabled(False)
        self.lineEditEfectivo.setEnabled(False)
        self.botonFactura = QPushButton('Ver Factura')
        self.botonFactura.setStyleSheet('QPushButton{font: 12pt; border-radius: 3px}')
        self.botonFactura.setFixedHeight(26)
        self.botonFactura.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButtonNuevaCompra.setEnabled(False)
        self.pushButtonNuevaCompra.setStyleSheet('QPushButton{color: black; font: 12pt;}')

        self.pushButtonFacturas.clicked.connect(self.listaFacturas)

        self.pushButtonPagar.clicked.connect(self.pagar)
        self.botonFactura.clicked.connect(self.mostrarFactura)
        self.botonClickeado()

    def botonClickeado(self):
        self.pushButton1.clicked.connect(self.crearListaCompra)
        self.pushButton2.clicked.connect(self.crearListaCompra)
        self.pushButton3.clicked.connect(self.crearListaCompra)
        self.pushButton4.clicked.connect(self.crearListaCompra)
        self.pushButton5.clicked.connect(self.crearListaCompra)
        self.pushButton6.clicked.connect(self.crearListaCompra)
        self.pushButton7.clicked.connect(self.crearListaCompra)
        self.pushButton8.clicked.connect(self.crearListaCompra)
        self.pushButton9.clicked.connect(self.crearListaCompra)
        self.pushButton10.clicked.connect(self.crearListaCompra)
        self.pushButton11.clicked.connect(self.crearListaCompra)
        self.pushButton12.clicked.connect(self.crearListaCompra)
        self.pushButton13.clicked.connect(self.crearListaCompra)
        self.pushButton14.clicked.connect(self.crearListaCompra)
        self.pushButton15.clicked.connect(self.crearListaCompra)
        self.pushButton16.clicked.connect(self.crearListaCompra)
        self.pushButton17.clicked.connect(self.crearListaCompra)
        self.pushButton18.clicked.connect(self.crearListaCompra)

    def crearListaCompra(self):
        boton = self.sender().objectName()
        self.pushButtonPagar.setEnabled(True)

        if boton == 'pushButton1':
            self.__controller.crearAntibiotico('KYROVET® Kyrotilm Oral X 240ml', '20mg/Kg peso', 'Ave', 6900)
            producto = QLabel('KYROVET® Kyrotilm Oral X 240ml')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton2':
            self.__controller.crearAntibiotico('KYROVET® Florbiotico X 50ml', '1ml/15Kg peso', 'Bovino', 57300)
            producto = QLabel('KYROVET® Florbiotico X 50ml')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton3':
            self.__controller.crearAntibiotico("KYROVET® Kyropen X 12'UI", '1ml/18Kg peso', 'Equino', 42800)
            producto = QLabel("KYROVET® Kyropen X 12'UI")
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton4':
            self.__controller.crearAntibiotico('VICAR® Panamicina X 500ml', '1ml/10Kg peso', 'Caprino', 75800)
            producto = QLabel('VICAR® Panamicina X 500ml')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton5':
            self.__controller.crearAntibiotico('LIVERDET® Oxitetraciclina X 500ml', '1ml/10Kg peso', 'Ovino', 16900)
            producto = QLabel('LIVERDET® Oxitetraciclina X 500ml')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton6':
            self.__controller.crearAntibiotico('VETERLAND® Neo Tetramiland X 500gr', '1ml/10Kg peso', 'Porcino', 84700)
            producto = QLabel('VETERLAND® Neo Tetramiland X 500gr')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton7':
            self.__controller.crearPlaguicida('6293', 'AGITA® 1GB Sobre X 20g', 'Unico uso', 7200, 'Un día')
            producto = QLabel('AGITA® 1GB Sobre X 20g')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton8':
            self.__controller.crearPlaguicida('1400', 'DOW® Closer 240SC X 1Lt', 'Unico uso', 288300, 'Siete días')
            producto = QLabel('DOW® Closer 240SC X 1Lt')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton9':
            self.__controller.crearPlaguicida('1376', 'NUFARM® Clorpirifos 480 X 1Lt', 'Unico uso', 36500, 'No aplica')
            producto = QLabel('NUFARM® Clorpirifos 480 X 1Lt')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton10':
            self.__controller.crearPlaguicida('1533', 'BAYER® Larvin 375SC X 1Lt', 'Unico uso', 144800, 'Un día')
            producto = QLabel('BAYER® Larvin 375SC X 1Lt')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton11':
            self.__controller.crearPlaguicida('2593', 'BAYER® Sencor SC480 X 1Lt', 'Unico uso', 137000, 'No aplica')
            producto = QLabel('BAYER® Sencor SC480 X 1Lt')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton12':
            self.__controller.crearPlaguicida('8467', 'SYNGENTA® Amistar 50WG X 40g', 'Unico uso', 27300, 'Un día')
            producto = QLabel('SYNGENTA® Amistar 50WG X 40g')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton13':
            popUpCalendario = CalendarioWindow()
            popUpCalendario.show()
            popUpCalendario.exec_()

            fecha = popUpCalendario.fecha

            self.__controller.crearFertilizante('4545', 'FORZA® Urea X 1Kg', 'Treinta días', 8900, fecha)
            producto = QLabel('FORZA® Urea X 1Kg')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton14':
            popUpCalendario = CalendarioWindow()
            popUpCalendario.show()
            popUpCalendario.exec_()

            fecha = popUpCalendario.fecha

            self.__controller.crearFertilizante('6277', 'ANASAC® Fertilizante Pastos X 500g', 'Unico uso', 12900, fecha)
            producto = QLabel('ANASAC® Fertilizante Pastos X 500g')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton15':
            popUpCalendario = CalendarioWindow()
            popUpCalendario.show()
            popUpCalendario.exec_()

            fecha = popUpCalendario.fecha

            self.__controller.crearFertilizante('11721', 'DAVALIA® Fertilizante Orquídeas X 500ml', 'Quince días',
                                                19900, fecha)
            producto = QLabel('DAVALIA® Fertilizante Orquídeas X 500ml')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton16':
            popUpCalendario = CalendarioWindow()
            popUpCalendario.show()
            popUpCalendario.exec_()

            fecha = popUpCalendario.fecha

            self.__controller.crearFertilizante('5773', 'DAVALIA® Fertilizante Floración X 800g', 'Quince días',
                                                1900, fecha)
            producto = QLabel('DAVALIA® Fertilizante Floración X 800g')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton17':
            popUpCalendario = CalendarioWindow()
            popUpCalendario.show()
            popUpCalendario.exec_()

            fecha = popUpCalendario.fecha

            self.__controller.crearFertilizante('7763', 'FORZA® Fertilizante Triple 15 X 1Kg', 'Treinta días',
                                                7900, fecha)
            producto = QLabel('FORZA® Fertilizante Triple 15 X 1Kg')
            self.layoutCompra.addWidget(producto)
        elif boton == 'pushButton18':
            popUpCalendario = CalendarioWindow()
            popUpCalendario.show()
            popUpCalendario.exec_()

            fecha = popUpCalendario.fecha

            self.__controller.crearFertilizante('6978', 'FORZA® Fertilizante Oscomote X 2Kg', 'Cuatro meses',
                                                74900, fecha)
            producto = QLabel('FORZA® Fertilizante Oscomote X 2Kg')
            self.layoutCompra.addWidget(producto)

        precio = str(self.__controller.valorCompra)
        self.labelPrecio.setText('$'+ precio)

    def pagar(self):
        self.pushButtonPagar.setEnabled(False)
        self.lineEditCedula.setEnabled(True)
        self.lineEditEfectivo.setEnabled(True)
        self.groupBox2.setStyleSheet("QGroupBox QLineEdit{background-color: rgb(186, 223, 51);}")
        self.botonDatos.show()
        self.labelCliente.hide()

        for boton in self.buttonGroup.buttons():
            boton.setEnabled(False)

        self.gridLayout_2.addWidget(self.botonDatos, 2, 0)

        self.botonDatos.clicked.connect(self.compraInput)

    def compraInput(self):
        cedula = self.lineEditCedula.text()

        if '' in [cedula, self.lineEditEfectivo.text()]:
            pass
        else:
            self.__controller.efectivoRecibido = int(self.lineEditEfectivo.text())
            self.groupBox2.setStyleSheet("QGroupBox QLineEdit{background-color: rgb(133, 147, 39);}")
            self.lineEditCedula.setEnabled(False)
            self.lineEditEfectivo.setEnabled(False)
            self.pushButtonNuevaCompra.setEnabled(True)
            self.botonDatos.hide()
            self.labelCliente.show()
            self.gridLayout_2.addWidget(self.labelCliente, 3, 0, 1, 2)

            if cedula in self.__controller.listaClientes:
                self.labelCliente.setText('Cliente antiguo. Compra exitosa')
                nombre = self.__controller.listaClientes[cedula].nombre
            else:
                popUp = RegistrarClientePopUp()
                popUp.show()
                popUp.exec_()

                nombre = popUp.nombreCliente

                self.labelCliente.setText('Cliente nuevo añadido. Compra exitosa')
                self.__controller.crearCliente(nombre, cedula)

            tiempoActual = datetime.now()
            fechaCompra = tiempoActual.strftime('%Y-%m-%d')
            horaCompra = tiempoActual.strftime('%H:%M')
            self.__controller.crearFactura(fechaCompra, horaCompra, self.__controller.listaCompra, nombre, cedula)
            self.gridLayout_2.addWidget(self.botonFactura, 4, 0, 1, 2)
            self.botonFactura.show()

            self.pushButtonNuevaCompra.clicked.connect(self.resetear)

            self.lineEditCedula.clear()
            self.lineEditEfectivo.clear()

    def mostrarFactura(self):
        factura = FacturaWindow(self.__controller.listaFacturas[-1])
        factura.show()
        factura.exec_()

    def listaFacturas(self):
        if self.__controller.numFactura == 0:
            popUp = QMessageBox()
            popUp.setStyleSheet('*{font: 12pt Gill Sans MT; background-color: rgb(231, 202, 143)} '
                                'QPushButton{border-radius: 3px; color: rgb(231, 202, 143);}')
            popUp.setWindowTitle('Lista de facturas')
            popUp.setIcon(QMessageBox.Information)
            popUp.setText('No hay facturas guardadas.')
            popUp.show()
            popUp.exec_()
        else:
            listaFacturasWindow = ListaFacturasWindow(self.__controller.numFactura, self.__controller.listaFacturas)
            listaFacturasWindow.show()
            listaFacturasWindow.exec_()

    def resetear(self):
        self.pushButtonNuevaCompra.setEnabled(False)
        self.botonFactura.hide()
        self.labelCliente.setText('')
        self.labelCliente.hide()

        for boton in self.buttonGroup.buttons():
            boton.setEnabled(True)

        i = 0
        while i < self.layoutCompra.count():
            self.layoutCompra.itemAt(i).widget().deleteLater()
            i += 1

        self.labelPrecio.setText('')
        self.__controller.valorCompra = 0
        self.__controller.listaCompra = []


class ListaFacturasWindow(QDialog):
    def __init__(self, numFacturas, listaFacturas):
        super().__init__()

        uic.loadUi('Interfaz/lista_facturas.ui', self)

        self.move(90, 20)
        self.setWindowTitle('Lista de facturas')
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        with open('Interfaz/styles.css') as f:
            self.setStyleSheet(f.read())

        self.numFacturas = numFacturas
        self.listaFacturas = listaFacturas

        self.layoutFacturas = QGridLayout()
        self.layoutFacturas.setAlignment(QtCore.Qt.AlignTop)
        self.widgetFacturas = QWidget()
        self.widgetFacturas.setLayout(self.layoutFacturas)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widgetFacturas)
        self.scrollArea.setStyleSheet('QScrollArea QLabel{font-size: 12pt;}')

        self.mostrarListaFacturas()

    def mostrarListaFacturas(self):
        for i in range(self.numFacturas):
            labelNumFactura = QLabel(str(self.listaFacturas[i].numeroFactura))
            labelNumFactura.setFixedSize(42, 16)
            labelFechaFactura = QLabel(self.listaFacturas[i].fechaCompra)
            labelFechaFactura.setFixedSize(105, 16)
            self.layoutFacturas.addWidget(labelNumFactura, i, 0)
            self.layoutFacturas.addWidget(labelFechaFactura, i, 1)

            boton = QPushButton('VER FACTURA')
            boton.setCursor(QtCore.Qt.PointingHandCursor)
            boton.setObjectName(str(i))
            boton.setFixedSize(90, 26)
            boton.clicked.connect(self.mostrarFactura)
            self.layoutFacturas.addWidget(boton, i, 2)

    def mostrarFactura(self):
        boton = self.sender()
        pos = int(boton.objectName())

        factura = FacturaWindow(self.listaFacturas[pos])
        factura.show()
        factura.exec_()


class RegistrarClientePopUp(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle('Registro cliente nuevo')

        with open("Interfaz/styles.css") as f:
            self.setStyleSheet(f.read())

        self.VLayout = QVBoxLayout()
        self.VLayout.setAlignment(QtCore.Qt.AlignTop)
        self.label = QLabel('Ingrese el nombre del cliente:')
        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton('Ingresar')
        self.pushButton.setFixedSize(60, 30)
        self.pushButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.VLayout.addWidget(self.label)
        self.VLayout.addWidget(self.lineEdit)
        self.VLayout.addWidget(self.pushButton)
        self.setLayout(self.VLayout)

        self.nombreCliente = ''
        self.pushButton.clicked.connect(self.ingresar)

    def ingresar(self):
        if self.lineEdit.text() == '':
            pass
        else:
            self.nombreCliente = self.lineEdit.text()
            self.close()


class FacturaWindow(QDialog):
    def __init__(self, factura):
        super().__init__()
        uic.loadUi('Interfaz/factura.ui', self)

        QtGui.QFontDatabase.addApplicationFont('Interfaz/OCR-A Regular.ttf')

        self.move(960, 20)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        with open("Interfaz/styles.css") as f:
            self.setStyleSheet(f.read())

        self.fechaCompra = factura.fechaCompra
        self.horaCompra = factura.horaCompra
        self.listaCompra = factura.listaCompra
        self.nombreCliente = factura.cliente['Nombre']
        self.cedulaCliente = factura.cliente['Cedula']
        self.valorCompra = factura.valorTotal
        self.numFactura = factura.numeroFactura
        self.dineroRecibido = factura.efectivoRecibido
        self.cambio = self.dineroRecibido - self.valorCompra

        self.layoutProductos = QGridLayout()
        self.layoutProductos.setAlignment(QtCore.Qt.AlignTop)
        self.widgetProductos = QWidget()
        self.widgetProductos.setLayout(self.layoutProductos)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widgetProductos)
        self.scrollArea.setStyleSheet('QScrollArea QLabel{font-size: 9pt;}')

        self.labelsSetText()

    def labelsSetText(self):
        self.label4.setText(self.fechaCompra)
        self.label5.setText(self.horaCompra)
        self.label5.setAlignment(QtCore.Qt.AlignRight)
        self.label7.setText(str(self.numFactura))
        self.label7.setAlignment(QtCore.Qt.AlignRight)
        self.label11.setText(str(self.nombreCliente))
        self.label13.setText(str(self.cedulaCliente))
        self.label16.setText(str(self.valorCompra))
        self.label16.setAlignment(QtCore.Qt.AlignRight)
        self.label25.setText(str(self.dineroRecibido))
        self.label23.setText(str(self.cambio))

        i = 0
        while i < len(self.listaCompra):
            labelNombre = QLabel(self.listaCompra[i].nombre)
            labelPrecio = QLabel(str(self.listaCompra[i].precio))
            labelPrecio.setAlignment(QtCore.Qt.AlignRight)
            self.layoutProductos.addWidget(labelNombre, i, 0)
            self.layoutProductos.addWidget(labelPrecio, i, 1)
            i += 1

class CalendarioWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Interfaz/calendario.ui', self)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        with open("Interfaz/styles.css") as f:
            self.setStyleSheet(f.read())

        self.fecha = str(self.calendarWidget.selectedDate().toPyDate())
        self.labelFecha.setText(self.fecha)
        self.calendarWidget.selectionChanged.connect(self.mostrarFecha)
        self.pushButton.setStyleSheet('QPushButton{font: 12pt; border-radius: 3px;}')
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.boton)


    def mostrarFecha(self):
        self.fecha = str(self.calendarWidget.selectedDate().toPyDate())
        self.labelFecha.setText(self.fecha)

    def boton(self):
        self.close()