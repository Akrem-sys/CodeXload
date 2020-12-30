from PyQt5 import QtCore, QtGui, QtWidgets


class Calculator_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(258, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("QFrame{\n"
        "background-color: rgb(22, 24, 27);\n"
        "border-radius:2px;\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Tableboard = QtWidgets.QLineEdit(self.frame)
        self.Tableboard.setGeometry(QtCore.QRect(0, 70, 241, 81))
        self.Tableboard.setStyleSheet("QLineEdit{\n"
        "border-radius:5px;\n"
        "background-color: rgb(31, 33, 38);\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:30pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "")
        self.Tableboard.setReadOnly(True)
        self.Tableboard.setObjectName("Tableboard")
        self.Num8 = QtWidgets.QPushButton(self.frame)
        self.Num8.setGeometry(QtCore.QRect(60, 210, 61, 51))
        self.Num8.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num8.setObjectName("Num8")
        self.Num7 = QtWidgets.QPushButton(self.frame)
        self.Num7.setGeometry(QtCore.QRect(0, 210, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.Num7.setFont(font)
        self.Num7.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num7.setObjectName("Num7")
        self.Multiply = QtWidgets.QPushButton(self.frame)
        self.Multiply.setGeometry(QtCore.QRect(180, 210, 61, 51))
        self.Multiply.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Multiply.setObjectName("Multiply")
        self.Num9 = QtWidgets.QPushButton(self.frame)
        self.Num9.setGeometry(QtCore.QRect(120, 210, 61, 51))
        self.Num9.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num9.setObjectName("Num9")
        self.Delete = QtWidgets.QPushButton(self.frame)
        self.Delete.setGeometry(QtCore.QRect(120, 160, 61, 51))
        self.Delete.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Delete.setObjectName("Delete")
        self.Devise = QtWidgets.QPushButton(self.frame)
        self.Devise.setGeometry(QtCore.QRect(180, 160, 61, 51))
        self.Devise.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Devise.setObjectName("Devise")
        self.CE = QtWidgets.QPushButton(self.frame)
        self.CE.setGeometry(QtCore.QRect(0, 160, 61, 51))
        self.CE.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.CE.setObjectName("CE")
        self.C = QtWidgets.QPushButton(self.frame)
        self.C.setGeometry(QtCore.QRect(60, 160, 61, 51))
        self.C.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.C.setObjectName("C")
        self.Num3 = QtWidgets.QPushButton(self.frame)
        self.Num3.setGeometry(QtCore.QRect(120, 310, 61, 51))
        self.Num3.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num3.setObjectName("Num3")
        self.Addition = QtWidgets.QPushButton(self.frame)
        self.Addition.setGeometry(QtCore.QRect(180, 310, 61, 51))
        self.Addition.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Addition.setObjectName("Addition")
        self.Num1 = QtWidgets.QPushButton(self.frame)
        self.Num1.setGeometry(QtCore.QRect(0, 310, 61, 51))
        self.Num1.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num1.setObjectName("Num1")
        self.Minus = QtWidgets.QPushButton(self.frame)
        self.Minus.setGeometry(QtCore.QRect(180, 260, 61, 51))
        self.Minus.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Minus.setObjectName("Minus")
        self.Num4 = QtWidgets.QPushButton(self.frame)
        self.Num4.setGeometry(QtCore.QRect(0, 260, 61, 51))
        self.Num4.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num4.setObjectName("Num4")
        self.Num2 = QtWidgets.QPushButton(self.frame)
        self.Num2.setGeometry(QtCore.QRect(60, 310, 61, 51))
        self.Num2.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num2.setObjectName("Num2")
        self.Num6 = QtWidgets.QPushButton(self.frame)
        self.Num6.setGeometry(QtCore.QRect(120, 260, 61, 51))
        self.Num6.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num6.setObjectName("Num6")
        self.Num5 = QtWidgets.QPushButton(self.frame)
        self.Num5.setGeometry(QtCore.QRect(60, 260, 61, 51))
        self.Num5.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num5.setObjectName("Num5")
        self.Negate = QtWidgets.QPushButton(self.frame)
        self.Negate.setGeometry(QtCore.QRect(0, 360, 61, 51))
        self.Negate.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Negate.setObjectName("Negate")
        self.Commas = QtWidgets.QPushButton(self.frame)
        self.Commas.setEnabled(True)
        self.Commas.setGeometry(QtCore.QRect(120, 360, 61, 51))
        self.Commas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Commas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Commas.setAutoFillBackground(False)
        self.Commas.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Commas.setAutoDefault(False)
        self.Commas.setObjectName("Commas")
        self.Num0 = QtWidgets.QPushButton(self.frame)
        self.Num0.setGeometry(QtCore.QRect(60, 360, 61, 51))
        self.Num0.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Num0.setObjectName("Num0")
        self.Equal = QtWidgets.QPushButton(self.frame)
        self.Equal.setGeometry(QtCore.QRect(180, 360, 61, 51))
        self.Equal.setStyleSheet("QPushButton{\n"
        "background-color: rgb(31, 33, 38);\n"
        "border-radius:1px;\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:40pt;\n"
        "font-weight:bold;\n"
        "color: rgb(199, 106, 12);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(22, 24, 27);\n"
        "}")
        self.Equal.setObjectName("Equal")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 241, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 150, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget{\n"
        "color: rgb(199, 106, 12);\n"
        "}")
        self.label.setObjectName("label")
        self.Close = QtWidgets.QPushButton(self.frame_2)
        self.Close.setEnabled(True)
        self.Close.setGeometry(QtCore.QRect(216, 0, 24, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Close.setFont(font)
        self.Close.setStyleSheet("QPushButton{\n"
        "border-radius:1px;\n"
        "background-color: rgb(22, 24, 27);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(232, 39, 21);\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:10pt;\n"
        "font-weight:bold;\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.Close.setObjectName("Close")
        self.Mini = QtWidgets.QPushButton(self.frame_2)
        self.Mini.setEnabled(True)
        self.Mini.setGeometry(QtCore.QRect(190, 0, 24, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Mini.setFont(font)
        self.Mini.setStyleSheet("QPushButton{\n"
        "border-radius:1px;\n"
        "background-color: rgb(22, 24, 27);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(31, 33, 38);\n"
        "}\n"
        "QWidget{\n"
        "font-family: Segoe UI;\n"
        "font-size:20pt;\n"
        "font-weight:bold;\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.Mini.setObjectName("Minimize")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Num8.setText(_translate("MainWindow", "8"))
        self.Num7.setText(_translate("MainWindow", "7"))
        self.Multiply.setText(_translate("MainWindow", "*"))
        self.Num9.setText(_translate("MainWindow", "9"))
        self.Delete.setText(_translate("MainWindow", "♣"))
        self.Devise.setText(_translate("MainWindow", "÷"))
        self.CE.setText(_translate("MainWindow", "CE"))
        self.C.setText(_translate("MainWindow", "C"))
        self.Num3.setText(_translate("MainWindow", "3"))
        self.Addition.setText(_translate("MainWindow", "+"))
        self.Num1.setText(_translate("MainWindow", "1"))
        self.Minus.setText(_translate("MainWindow", "-"))
        self.Num4.setText(_translate("MainWindow", "4"))
        self.Num2.setText(_translate("MainWindow", "2"))
        self.Num6.setText(_translate("MainWindow", "6"))
        self.Num5.setText(_translate("MainWindow", "5"))
        self.Negate.setText(_translate("MainWindow", "±"))
        self.Commas.setText(_translate("MainWindow", ","))
        self.Num0.setText(_translate("MainWindow", "0"))
        self.Equal.setText(_translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", "Akrem Calculator"))
        self.Close.setToolTip(_translate("MainWindow", "<html><head/><body><p>X</p></body></html>"))
        self.Close.setText(_translate("MainWindow", "X"))
        self.Mini.setToolTip(_translate("MainWindow", "<html><head/><body><p>X</p></body></html>"))
        self.Mini.setText(_translate("MainWindow", "-"))


