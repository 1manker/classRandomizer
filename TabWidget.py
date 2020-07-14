#RandMainView.py
#Lucas Manker
#subclass of QWidget

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TabWidget(QWidget):

	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
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
		self._createButtons()

		#add the tabs
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)

	def _createButtons(self):

		buttonsLayout = QGridLayout()

		#top three buttons
		self.b1 = QPushButton('Upload Class List')
		buttonsLayout.addWidget(self.b1, 0, 0)
		self.b1.clicked.connect(lambda:self.whichbtn(self.b1))

		self.b2 = QPushButton('View Class List')
		buttonsLayout.addWidget(self.b2, 0, 1)
		self.b2.clicked.connect(lambda:self.whichbtn(self.b2))

		self.b3 = QPushButton('Edit Class List')
		buttonsLayout.addWidget(self.b3, 0, 2)
		self.b3.clicked.connect(lambda:self.whichbtn(self.b3))

		#text box for class list
		self.info = QTextBrowser(self.tab1)
		self.info.setMinimumHeight(100)
		self.info.setMaximumHeight(200)
		buttonsLayout.addWidget(self.info, 1, 0, 3, 0)

		buttonsLayout.setContentsMargins(25,25,25,25)
		buttonsLayout.setAlignment(Qt.AlignTop)
		self.tab1.setLayout(buttonsLayout)

	def whichbtn(self,b):
		#figures out what button is clicked, then does stuff
		print("clicked buttons is " + b.text())
		if(b.text() == 'Upload Class List'):
			self.getfiles()

	def getfiles(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;", options=options)
		if fileName:
			print(fileName[0])
			f = open(fileName[0], 'r')
			self.info.setText(f.read())
			f.close()
