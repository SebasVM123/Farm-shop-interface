from GUI import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = TiendaAgricola()
    GUI.show()
    sys.exit(app.exec_())