import codecs
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
		self.st = self.textEdit.toPlainText()
		self.mas = ['!','.',',','?','-',':',';']
		for x in range(len(self.mas)):
			self.st = self.st.replace(self.mas[x],'')
		self.st = self.st.split(' ')
		i = 0
		while i < len(self.st):
			if self.st[i] == '':
				del self.st[i]
			else:
				i += 1
		self.st_ = ''
		for x in range(len(self.st)):
			if x == len(self.st)-1:
				self.st_+=self.st[x]+'.'
			else:
				self.st_+=self.st[x]+', '
		self.textEdit_2.setPlainText(self.st_)
			#print(self.st[x]+'\n')

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())