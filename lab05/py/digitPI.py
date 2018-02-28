import time
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox, QLabel
#from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.uic import loadUi

results, appx = [], []

def timer(f):
	def tmp(*args, **kwargs):
		t = time.time()
		res = f(*args, **kwargs)
		appx.append(round((time.time()-t),2)); appx.append("Нет")
		results.append(appx)
		return res
	return tmp

def f(n):
	return ((-1)**(n+1))/(2*n-1)

@timer
def pi(eps):
	global appx
	n,s,s1,s2 = 1,0,0,0
	while (True):
		s1 = f(n); s2 = f(n+1); s+=f(n)
		n+=1
		if abs(s2-s1) <= eps:
			break
	appx.append(4*s)

def start(x1,x2, pg):
	global appx
	total = 0
	p = 0
	for i in range(x1,x2,-1):
		appx = []
		appx.append('10^'+str(i))
		pi(10**i); p+=1
		pg.setValue(int((100/abs(x2-x1))*p))
	for i in range(len(results)):
		if (i > 1):
			a = str(results[i][1])
			b = str(results[i-1][1])
			a = a[0:9]; b = b[0:9]
			if (a == b):
				results[i][3] = "Да"
	for i in range(len(results)):
		if i > 0:
			c = results[i][2]
			total+=c
		for j in range(len(results[i])):
			print(results[i][j], end=' ')
		print()
	total = round(total,2)
	return total

class MyTableModel(QAbstractTableModel):
	def __init__(self, datain, headerdata, parent=None):
		QAbstractTableModel.__init__(self, parent)
		self.arraydata = datain
		self.headerdata = headerdata
	def rowCount(self, parent):
		return len(self.arraydata)

	def columnCount(self, parent):
		if len(self.arraydata) > 0: 
			return len(self.arraydata[0]) 
		return 0

	def data(self, index, role):
		if not index.isValid():
			return QVariant()
		elif role != Qt.DisplayRole:
			return QVariant()
		return QVariant(self.arraydata[index.row()][index.column()])

	def setData(self, index, value, role):
		pass         # not sure what to put here

	def headerData(self, col, orientation, role):
		if orientation == Qt.Horizontal and role == Qt.DisplayRole:
			return QVariant(self.headerdata[col])
		return QVariant()

class Window(QMainWindow):
	def __init__(self):
		self.st = ''
		QMainWindow.__init__(self)
		loadUi('UI.ui',self)

	@pyqtSlot()
	def on_pushButton_clicked(self):
		print('start calculate')
		global results
		results = []
		self.tableView.clearSpans()
		x1 = self.lineEdit_2.text()
		x2 = self.lineEdit.text()
		self.progressBar.setValue(0)
		ret = start(int(x1),int(x2)-1, self.progressBar)
		self.label_4.setText('Общее время: '+str(ret))
		header = ['Точность', 'Число Пи', 'Время (с.)', '7 знаков постоянны']
		tablemodel = MyTableModel(results, header, self)
		self.tableView.setModel(tablemodel)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWin = Window()
	mainWin.show()
	sys.exit(app.exec_())


