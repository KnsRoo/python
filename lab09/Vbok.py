import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('UI.ui',self)
		self.a = str(QMessageBox.Ok > QMessageBox.Cancel and QMessageBox.Critical < QMessageBox.Question)
		self.label.setText(self.a)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())
	#print(QMessageBox.Ok > QMessageBox.Cancel and QMessageBox.Critical < QMessageBox.Question)