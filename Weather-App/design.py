from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 388)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.inputCidade = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCidade.setGeometry(QtCore.QRect(90, 90, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.inputCidade.setFont(font)
        self.inputCidade.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputCidade.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.inputCidade.setAlignment(QtCore.Qt.AlignCenter)
        self.inputCidade.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputCidade.setClearButtonEnabled(False)
        self.inputCidade.setObjectName("inputCidade")
        self.btn_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enviar.setGeometry(QtCore.QRect(150, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_enviar.setFont(font)
        self.btn_enviar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_enviar.setObjectName("btn_enviar")
        self.label_min = QtWidgets.QLabel(self.centralwidget)
        self.label_min.setGeometry(QtCore.QRect(130, 290, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_min.setFont(font)
        self.label_min.setObjectName("label_min")
        self.label_max = QtWidgets.QLabel(self.centralwidget)
        self.label_max.setGeometry(QtCore.QRect(130, 310, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_max.setFont(font)
        self.label_max.setObjectName("label_max")
        self.label_city = QtWidgets.QLabel(self.centralwidget)
        self.label_city.setGeometry(QtCore.QRect(30, 240, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_city.setFont(font)
        self.label_city.setObjectName("label_city")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(30, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_temp.setFont(font)
        self.label_temp.setObjectName("label_temp")
        self.label_desc = QtWidgets.QLabel(self.centralwidget)
        self.label_desc.setGeometry(QtCore.QRect(30, 350, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_desc.setFont(font)
        self.label_desc.setObjectName("label_desc")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(240, 250, 141, 101))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_tempmin = QtWidgets.QLabel(self.centralwidget)
        self.label_tempmin.setGeometry(QtCore.QRect(170, 280, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_tempmin.setFont(font)
        self.label_tempmin.setObjectName("label_tempmin")
        self.label_tempmax = QtWidgets.QLabel(self.centralwidget)
        self.label_tempmax.setGeometry(QtCore.QRect(170, 310, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_tempmax.setFont(font)
        self.label_tempmax.setObjectName("label_tempmax")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(280, 350, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_time.setObjectName("label_time")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 210, 271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_stermica = QtWidgets.QLabel(self.centralwidget)
        self.label_stermica.setGeometry(QtCore.QRect(130, 330, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_stermica.setFont(font)
        self.label_stermica.setObjectName("label_stermica")
        self.label_stermica2 = QtWidgets.QLabel(self.centralwidget)
        self.label_stermica2.setGeometry(QtCore.QRect(190, 330, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_stermica2.setFont(font)
        self.label_stermica2.setObjectName("label_stermica2")
        self.btnInfo = QtWidgets.QPushButton(self.centralwidget)
        self.btnInfo.setGeometry(QtCore.QRect(10, 3, 21, 20))
        self.btnInfo.setText("")
        self.btnInfo.setObjectName("btnInfo")
        self.btnInfo.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                   "border-radius: 10px;")
        self.btn_enviar.setObjectName("btn_enviar")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 3, 21, 20))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(''
                                        'background-color: rgb(255, 85, 0);'
                                        'border-radius: 10px;')
        self.label_img.raise_()
        self.label.raise_()
        self.inputCidade.raise_()
        self.btn_enviar.raise_()
        self.label_min.raise_()
        self.label_max.raise_()
        self.label_city.raise_()
        self.label_temp.raise_()
        self.label_desc.raise_()
        self.label_tempmin.raise_()
        self.label_tempmax.raise_()
        self.label_time.raise_()
        self.line.raise_()
        self.label_stermica.raise_()
        self.label_stermica2.raise_()
        self.btnInfo.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qual a temperatura?"))
        self.label.setText(_translate("MainWindow", "Qual a temperatura?"))
        self.inputCidade.setText(_translate("MainWindow", "Digite a cidade"))
        self.inputCidade.setPlaceholderText(_translate("MainWindow", "Digite a cidade"))
        self.btn_enviar.setText(_translate("MainWindow", "Enviar"))