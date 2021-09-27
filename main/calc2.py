from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 531)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowOpacity(0.96)
        MainWindow.setStyleSheet("background-color: rgb(53, 50, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.OutputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.OutputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OutputLabel.setLineWidth(2)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        self.PercentButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.PercentButtom.setGeometry(QtCore.QRect(6, 110, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.PercentButtom.setFont(font)
        self.PercentButtom.setMouseTracking(False)
        self.PercentButtom.setAcceptDrops(False)
        self.PercentButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.PercentButtom.setFlat(False)
        self.PercentButtom.setObjectName("PercentButtom")
        self.cButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.cButtom.setGeometry(QtCore.QRect(94, 110, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButtom.setFont(font)
        self.cButtom.setAutoFillBackground(False)
        self.cButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.cButtom.setFlat(False)
        self.cButtom.setObjectName("cButtom")
        self.arrowButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.arrowButtom.setGeometry(QtCore.QRect(182, 110, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButtom.setFont(font)
        self.arrowButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.arrowButtom.setFlat(False)
        self.arrowButtom.setObjectName("arrowButtom")
        self.drvideButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.drvideButtom.setGeometry(QtCore.QRect(270, 110, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.drvideButtom.setFont(font)
        self.drvideButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.drvideButtom.setFlat(False)
        self.drvideButtom.setObjectName("drvideButtom")
        self.eightButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eightButtom.setGeometry(QtCore.QRect(94, 190, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButtom.setFont(font)
        self.eightButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.eightButtom.setFlat(False)
        self.eightButtom.setObjectName("eightButtom")
        self.multiplyButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiplyButtom.setGeometry(QtCore.QRect(270, 190, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButtom.setFont(font)
        self.multiplyButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.multiplyButtom.setFlat(False)
        self.multiplyButtom.setObjectName("multiplyButtom")
        self.sevenButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.sevenButtom.setGeometry(QtCore.QRect(6, 190, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButtom.setFont(font)
        self.sevenButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.sevenButtom.setFlat(False)
        self.sevenButtom.setObjectName("sevenButtom")
        self.nineButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nineButtom.setGeometry(QtCore.QRect(182, 190, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButtom.setFont(font)
        self.nineButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.nineButtom.setAutoDefault(False)
        self.nineButtom.setFlat(False)
        self.nineButtom.setObjectName("nineButtom")
        self.oneButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.oneButtom.setGeometry(QtCore.QRect(6, 350, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButtom.setFont(font)
        self.oneButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.oneButtom.setFlat(False)
        self.oneButtom.setObjectName("oneButtom")
        self.fiveButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.fiveButtom.setGeometry(QtCore.QRect(94, 270, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButtom.setFont(font)
        self.fiveButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.fiveButtom.setFlat(False)
        self.fiveButtom.setObjectName("fiveButtom")
        self.minusButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusButtom.setGeometry(QtCore.QRect(270, 270, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButtom.setFont(font)
        self.minusButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.minusButtom.setFlat(False)
        self.minusButtom.setObjectName("minusButtom")
        self.fourButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.fourButtom.setGeometry(QtCore.QRect(6, 270, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButtom.setFont(font)
        self.fourButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.fourButtom.setFlat(False)
        self.fourButtom.setObjectName("fourButtom")
        self.sixButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sixButtom.setGeometry(QtCore.QRect(182, 270, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButtom.setFont(font)
        self.sixButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.sixButtom.setFlat(False)
        self.sixButtom.setObjectName("sixButtom")
        self.twoButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.twoButtom.setGeometry(QtCore.QRect(94, 350, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButtom.setFont(font)
        self.twoButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.twoButtom.setFlat(False)
        self.twoButtom.setObjectName("twoButtom")
        self.threeButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.threeButtom.setGeometry(QtCore.QRect(182, 350, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButtom.setFont(font)
        self.threeButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.threeButtom.setFlat(False)
        self.threeButtom.setObjectName("threeButtom")
        self.addButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.addButtom.setGeometry(QtCore.QRect(270, 350, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButtom.setFont(font)
        self.addButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.addButtom.setFlat(False)
        self.addButtom.setObjectName("addButtom")
        self.ecualButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.ecualButtom.setGeometry(QtCore.QRect(270, 430, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ecualButtom.setFont(font)
        self.ecualButtom.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ecualButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.ecualButtom.setFlat(False)
        self.ecualButtom.setObjectName("ecualButtom")
        self.decimalButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimalButtom.setGeometry(QtCore.QRect(182, 430, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButtom.setFont(font)
        self.decimalButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.decimalButtom.setFlat(False)
        self.decimalButtom.setObjectName("decimalButtom")
        self.plusMinusButtom = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.plus_minus_it()) 
        self.plusMinusButtom.setGeometry(QtCore.QRect(6, 430, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusButtom.setFont(font)
        self.plusMinusButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(30, 39, 46);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(47, 54, 64);\n"
"}")
        self.plusMinusButtom.setFlat(False)
        self.plusMinusButtom.setObjectName("plusMinusButtom")
        self.zeroButtom = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zeroButtom.setGeometry(QtCore.QRect(94, 430, 86, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButtom.setFont(font)
        self.zeroButtom.setStyleSheet("QPushButton{\n"
"color: rgb(255, 247, 247);\n"
"background-color: rgb(99, 110, 114);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 142, 155);\n"
"}")
        self.zeroButtom.setFlat(False)
        self.zeroButtom.setObjectName("zeroButtom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # My functional code

    # Remove character
    def remove_it(self):
            # Grab whats's on the screen already
            screen = self.OutputLabel.text()
            # Remove last item in list/string
            screen = screen[:-1]
            # Output back to the screen
            self.OutputLabel.setText(screen)

    # Mathematical calculation
    def math_it(self):
            # Grab whats's on the screen already
            screen = self.OutputLabel.text()
            try:
                # Do the math
                answer = eval(screen)
                # Output answer to the screen 
                self.OutputLabel.setText(str(answer))
            except:
                # Output error to the screen
                self.OutputLabel.setText("ERROR")
    # Change from positive/negative
    def plus_minus_it(self):
            # Grab whats's on the screen already
            screen = self.OutputLabel.text()
            if "-" in screen:
                screen = self.OutputLabel.setText(screen.replace("-", ""))
            else:
                self.OutputLabel.setText(f'-{screen}')


    # Add decimal
    def dot_it(self):
            # Grab whats's on the screen already
        screen = self.OutputLabel.text()
        if screen[-1] == ".":
                pass
        else:
                self.OutputLabel.setText(f'{screen}.')

    

    def press_it(self,pressed):
        if pressed == "C":
                self.OutputLabel.setText("0")
        else:
             # Check to see starts 0 
             if self.OutputLabel.text() == "0":
                     self.OutputLabel.setText("")
                # concatenate the pressed button whit what was there already
             self.OutputLabel.setText(f' {self.OutputLabel.text()}{pressed}')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        self.OutputLabel.setText(_translate("MainWindow", "0"))
        self.PercentButtom.setText(_translate("MainWindow", "%"))
        self.cButtom.setText(_translate("MainWindow", "C"))
        self.arrowButtom.setText(_translate("MainWindow", "<<"))
        self.drvideButtom.setText(_translate("MainWindow", "/"))
        self.eightButtom.setText(_translate("MainWindow", "8"))
        self.multiplyButtom.setText(_translate("MainWindow", "X"))
        self.sevenButtom.setText(_translate("MainWindow", "7"))
        self.nineButtom.setText(_translate("MainWindow", "9"))
        self.oneButtom.setText(_translate("MainWindow", "1"))
        self.fiveButtom.setText(_translate("MainWindow", "5"))
        self.minusButtom.setText(_translate("MainWindow", "-"))
        self.fourButtom.setText(_translate("MainWindow", "4"))
        self.sixButtom.setText(_translate("MainWindow", "6"))
        self.twoButtom.setText(_translate("MainWindow", "2"))
        self.threeButtom.setText(_translate("MainWindow", "3"))
        self.addButtom.setText(_translate("MainWindow", "+"))
        self.ecualButtom.setText(_translate("MainWindow", "="))
        self.decimalButtom.setText(_translate("MainWindow", "."))
        self.plusMinusButtom.setText(_translate("MainWindow", "+/-"))
        self.zeroButtom.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
