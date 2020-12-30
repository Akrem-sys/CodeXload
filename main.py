import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  Qt,QCoreApplication
from PyQt5.QtWidgets import QMainWindow,QApplication
from Calculator_gui import *

class Winner(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Calculator_UI()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        def write(x):
            ch=self.ui.Tableboard.text()
            if len(ch)>0 and ch[len(ch)-1] in mode and x in mode:
                ch=list(ch)
                ch[len(ch)-1]=x
                ch="".join(ch)
                self.ui.Tableboard.setText(ch)
            elif len(ch)==0 and x in ["*","+","/"]:
                pass
            else:
                ch=ch+str(x)
                self.ui.Tableboard.setText(ch)
                fontchanger(len(ch))

        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:  
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        def calculate():
            ch=self.ui.Tableboard.text()
            if ch[len(ch)-1] in mode:
                ch=list(ch)
                ch[len(ch)-1]=""
                ch="".join(ch)
            x=eval(ch)
            fontchanger(len(str(x)))
            self.ui.Tableboard.setText(str(x))
        def fontchanger(x):
            if a-(x//6)*5>5:
                l=str(a-(x//6)*5)
                self.ui.Tableboard.setStyleSheet("QLineEdit{\n"
                "border-radius:5px;\n"
                "background-color: rgb(31, 33, 38);\n"
                "}\n"
                "QWidget{\n"
                "font-family: Segoe UI;\n"
                "font-size:"+l+"pt;\n"
                "font-weight:bold;\n"
                "color: rgb(199, 106, 12);\n"
                "}\n"
                "")
        def delete():
            ch=self.ui.Tableboard.text()
            if len(ch)!=0:
                ch=list(ch)
                ch[len(ch)-1]=""
                ch="".join(ch)
                self.ui.Tableboard.setText(ch)
        def negate():
            ch=self.ui.Tableboard.text()
            if len(ch)!=0:
                if ch[0].isdigit():
                    ch="-"+ch
                else:
                    ch=list(ch)
                    ch[0]=""
                    ch="".join(ch)
                self.ui.Tableboard.setText(ch)

        self.ui.frame_2.mouseMoveEvent = moveWindow
        self.ui.Mini.clicked.connect(lambda: self.showMinimized())
        self.ui.Close.clicked.connect(QCoreApplication.instance().quit)
        self.ui.Num0.clicked.connect(lambda: write(0))
        self.ui.Num1.clicked.connect(lambda: write(1))
        self.ui.Num2.clicked.connect(lambda: write(2))
        self.ui.Num3.clicked.connect(lambda: write(3))
        self.ui.Num4.clicked.connect(lambda: write(4))
        self.ui.Num5.clicked.connect(lambda: write(5))
        self.ui.Num6.clicked.connect(lambda: write(6))
        self.ui.Num7.clicked.connect(lambda: write(7))
        self.ui.Num8.clicked.connect(lambda: write(8))
        self.ui.Num9.clicked.connect(lambda: write(9))
        self.ui.Devise.clicked.connect(lambda: write("/"))
        self.ui.Multiply.clicked.connect(lambda: write("*"))
        self.ui.Minus.clicked.connect(lambda: write("-"))
        self.ui.Addition.clicked.connect(lambda: write("+"))
        self.ui.Equal.clicked.connect(calculate)
        self.ui.Delete.clicked.connect(delete)
        self.ui.Commas.clicked.connect(lambda: write("."))
        self.ui.C.clicked.connect(lambda: self.ui.Tableboard.setText(""))
        self.ui.CE.clicked.connect(lambda: self.ui.Tableboard.setText(""))
        self.ui.Negate.clicked.connect(negate)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
if __name__ == "__main__":
    global mode,a
    a=30
    mode=["*","-","/","+"]
    app = QApplication(sys.argv)
    window = Winner()
    sys.exit(app.exec_())