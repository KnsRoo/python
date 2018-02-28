import datetime
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi

class Window(QMainWindow):
	def __init__(self):
		self.a = ''
		QMainWindow.__init__(self)
		loadUi('UI.ui',self)

	@pyqtSlot()
	def on_pushButton_clicked(self):
		self.a = self.lineEdit.text()
		self.a = self.a.split('.')
		self.now = datetime.datetime.today()
		self.year = self.now.year - int(self.a[2]) -1
		self.month = self.now.month + (12-int(self.a[1])) - 1
		self.day = self.now.day + (31 - int(self.a[0])) + 1
		if self.day > 31:
			self.day-=31; self.month+=1;
		if self.month > 12:
			self.month-=12; self.year+=1;
		self.label_2.setText("Стаж работы "+str(self.year)+" года(лет) "+str(self.month)+" месяцев "+str(self.day)+" дней(дня) ")

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())


