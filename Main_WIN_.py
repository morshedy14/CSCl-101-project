from PyQt5 import QtCore, QtGui, QtWidgets
from Welcome_Class_Analysis import Ui_Wlcome_Class_Analysis
from Personal_Grade_GUI import Ui_Main_Personal_Grade


class Ui_MainWindow(object):

    def pop_personal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main_Personal_Grade()
        self.ui.setupUi(self.window)
        self.window.show()

    def pop_Class_Analysis(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Wlcome_Class_Analysis()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(95, -10, 455, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pop_personal())
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(16)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pop_Class_Analysis())
        self.pushButton_2.setGeometry(QtCore.QRect(370, 130, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "What do you want to calculate?"))
        self.pushButton.setText(_translate("MainWindow", "Personal Grade"))
        self.pushButton_2.setText(_translate("MainWindow", "Class Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
