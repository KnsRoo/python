import random
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi


def floatc():
	u = random.uniform(-20.0,20.0)
	return round(u,3)

def createarray(n, par, self):
	x, y, xcp = [floatc() for j in range(n)], [], 0
	for i in range(len(x)):
		a = x[i]/len(x); xcp+=a;
	for i in range(len(x)):
		b = round(x[i]/xcp,3); y.append(b)
	stx,sty = 'x = (','y = ('
	for i in range(len(x)):
		if i == len(x)-1:
			stx+=str(x[i])+')'
			sty+=str(y[i])+')'
		else:
			stx+=str(x[i])+', '
			sty+=str(y[i])+', '
	if par == 1:
		self.textEdit.setPlainText(stx+'\n'+sty)
	elif par == 2:
		self.textEdit_2.setPlainText(stx+'\n'+sty)
	else:
		self.textEdit_3.setPlainText(stx+'\n'+sty)

class Window(QMainWindow):
	def __init__(self):
		self.st = ''
		QMainWindow.__init__(self)
		loadUi('UI.ui',self)

	@pyqtSlot()
	def on_pushButton_clicked(self):
		self.a = int(self.lineEdit_3.text())
		self.b = int(self.lineEdit_2.text())
		self.c = int(self.lineEdit.text())
		self.label_4.setText('n = '+str(self.a))
		self.label_5.setText('n = '+str(self.b))
		self.label_6.setText('n = '+str(self.c))
		createarray(self.a, 1, self)
		createarray(self.b, 2, self)
		createarray(self.c, 3, self)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())
