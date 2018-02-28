import math
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi

class Window(QMainWindow):
	def __init__(self):
		self.st = ''
		QMainWindow.__init__(self)
		loadUi('UI.ui',self)

	@pyqtSlot()
	def on_pushButton_clicked(self):
		self.a = float(self.lineEdit_3.text())
		self.b = float(self.lineEdit_2.text())
		self.c = float(self.lineEdit.text())
		res = ((3+(3+(math.tan(self.a)**2)/(32+self.b))**(1/3))**(1/3))+math.log10(self.a**3/(self.a+self.b+2*self.c))
		self.lineEdit_4.setText(str(res))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())
	#a, b, c = 3.1415, 96.6, 18.4
	#print(((3+(3+(math.tan(a)**2)/(32+b))**(1/3))**(1/3))+math.log10(a**3/(a+b+2*c)))