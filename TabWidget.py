#RandMainView.py
#Lucas Manker
#subclass of QWidget

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ClassList

class TabWidget(QWidget):

	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
		#list object to keep track of class list
		self.uploadedList = ClassList.ClassList()

		self.layout = QVBoxLayout(self)

		self.tabs = QTabWidget()
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tabs.resize(300,200)

		#three tabs...for now
		self.tabs.addTab(self.tab1, "Class List Properties")
		self.tabs.addTab(self.tab2, "Randomization")
		self.tabs.addTab(self.tab3, "Seating Chart")

		#add some buttons!
		self._createButtonsT1()
		self._createButtonsT2()

		#add the tabs
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

	def _createButtonsT1(self):

		buttonsLayout = QGridLayout()

		#top three buttons
		self.b1 = QPushButton('Upload Class List')
		buttonsLayout.addWidget(self.b1, 0, 0)
		self.b1.clicked.connect(lambda:self.whichbtn(self.b1))

		self.b2 = QPushButton('Save Class List')
		buttonsLayout.addWidget(self.b2, 0, 1)
		self.b2.clicked.connect(lambda:self.whichbtn(self.b2))

		self.b3 = QPushButton('Edit Class List')
		buttonsLayout.addWidget(self.b3, 0, 2)
		self.b3.clicked.connect(lambda:self.whichbtn(self.b3))

		#text box for class list
		self.info = QTextBrowser(self.tab1)
		self.info.setReadOnly(True)
		self.info.setMinimumHeight(100)
		self.info.setMaximumHeight(200)
		buttonsLayout.addWidget(self.info, 1, 0, 3, 0)

		buttonsLayout.setContentsMargins(25,25,25,25)
		buttonsLayout.setAlignment(Qt.AlignTop)
		self.tab1.setLayout(buttonsLayout)

	def whichbtn(self,b):
		#figures out what button is clicked, then does stuff
		if(b.text() == 'Upload Class List'):
			self.getList()
			self.info.setReadOnly(True)
		if(b.text() == 'Edit Class List'):
			self.info.setReadOnly(False)
		if(b.text() == 'Save Class List'):
			self.saveList()
			self.info.setReadOnly(True)
		if(b.text() == "Genders"):
			self.getGenderSplit()

	def getList(self):
		#opens file explorer for list upload
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;", options=options)
		if fileName:
			print(fileName[0])
			f = open(fileName[0], 'r')
			lines = f.readlines()
			#check for formatting
			for line in lines:
				split = line.split(',')
				if(len(split) != 4):
					#ask user if they still want to load bad file
					msg = QMessageBox()
					msg.setIcon(QMessageBox.Critical)
					msg.setText("List Improperly Formatted")
					msg.setInformativeText("Load Anyway?")
					msg.setWindowTitle("Error")
					msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
					ret = msg.exec()
					if(ret == QMessageBox.Cancel):
						self.info.setText('')
						f.close()
						return()
			#go back to beginning of file
			f.seek(0,0)
			#put the file contents in the textbox
			self.info.setText(f.read())
			self.uploadedList.importList(fileName[0])
			f.close()

	def saveList(self):
		#file explorer to save list
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()", "","All Files (*);;", options=options)
		if fileName:
			print(fileName)
			f = open(fileName, 'w')
			#convert contents of textbox to plain text and write to file
			text = self.info.toPlainText()
			f.write(text)
			f.close()

	#functions for tab2

	#general layout of tab2
	def _createButtonsT2(self):

		buttonsLayout = QGridLayout() 

		#determines if class list is uploaded and valid


		self.uploadValid = QTextBrowser(self.tab2)
		self.uploadValid.setReadOnly(True)
		self.uploadValid.setMaximumHeight(25)
		buttonsLayout.addWidget(self.uploadValid, 0, 0, 1, 0)
		self.uploadValid.setText("kek")

		self.b5 = QPushButton('Upload')
		buttonsLayout.addWidget(self.b5, 1, 2)

		self.b5.clicked.connect(lambda:self.whichbtn(self.b5))
		self.genderExp = QTextBrowser(self.tab2)
		self.genderExp.setReadOnly(True)
		self.genderExp.setMaximumHeight(25)
		self.genderExp.setMaximumWidth(250)
		buttonsLayout.addWidget(self.genderExp, 2, 0, 1, 0)
		self.genderExp.setText("LIST IS VALID")

		self.b4 = QPushButton('Genders')
		buttonsLayout.addWidget(self.b4, 3, 2)
		self.b4.clicked.connect(lambda:self.whichbtn(self.b4))

		buttonsLayout.setContentsMargins(25,25,25,25)
		buttonsLayout.setAlignment(Qt.AlignTop)
		self.tab2.setLayout(buttonsLayout)

	def getGenderSplit(self):
		strex = self.uploadedList.getGenderSplit()
		self.genderExp.setText(strex)