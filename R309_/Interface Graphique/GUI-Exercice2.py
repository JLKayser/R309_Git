import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox, \
    QDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.__aide = None

        widget = QWidget()
        self.resize(325,200)
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__temperature = QLabel("Temperature")
        self.__conv = QLabel("Conversion")
        self.__degre = QLineEdit("")
        self.__degre2 = QLineEdit("")
        self.__degre2.setDisabled(True)
        self.__C = QLabel("°C")
        self.__K = QLabel("K")
        self.__convertir = QPushButton("Convertir")
        self.__change = QComboBox()
        self.__change.addItems(['°C -> K','K -> °C'])
        self.__help = QPushButton("?")
        self.__change.activated[str].connect(self.__set_OnOff)

        grid.addWidget(self.__temperature, 0, 0)
        grid.addWidget(self.__degre, 0, 1)
        grid.addWidget(self.__C, 0, 2)
        grid.addWidget(self.__degre2,2, 1)
        grid.addWidget(self.__convertir, 1, 1)
        grid.addWidget(self.__change, 1, 2)
        grid.addWidget(self.__conv, 2, 0)
        grid.addWidget(self.__K, 2, 2)
        grid.addWidget(self.__help, 3, 2)


        self.__convertir.clicked.connect(self.__ConversionCK)
        self.__help.clicked.connect(self.__Help)
        self.setWindowTitle("Exercice-2")


    def __ConversionCK(self):
        try:
            var = float(self.__degre.text()) - 273.15
            self.__degre2.setText(str(var))
        except:
            self.__degre.setText("")
            self.__aaa()

    def __ConversionKC(self):
        try:
            var = float(self.__degre2.text()) + 273.15
            self.__degre.setText(str(var))
        except:
            self.__degre2.setText("")
            self.__aaa()


    def __set_OnOff(self,change):
        try:
            if change == 'K -> °C':
                self.__convertir.clicked.connect(self.__ConversionKC)
                self.__convertir.clicked.disconnect(self.__ConversionCK)
                self.__degre2.setDisabled(False)
                self.__degre.setDisabled(True)
            else:
                self.__convertir.clicked.connect(self.__ConversionCK)
                self.__convertir.clicked.disconnect(self.__ConversionKC)
                self.__degre2.setDisabled(True)
                self.__degre.setDisabled(False)
        except:
            pass


    def __Help(self):
        msg = QMessageBox()
        msg.setWindowTitle("Aide")
        msg.resize(500, 500)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Permet de convertir un nombre soit de Kelvin vers Celcuis, soit de Celcuis vers Kelvin.")
        msg.exec()

    def __aaa(self):
        msg = QMessageBox()
        msg.setWindowTitle("aaa")
        msg.resize(500, 500)
        msg.setIcon(QMessageBox.Critical)
        msg.setText("ENTREZ UN NOMBRE SVP !")
        msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()