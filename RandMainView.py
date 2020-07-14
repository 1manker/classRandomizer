#RandMainView.py
#Lucas Manker
#subclass of QMainWindow

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import TabWidget


class RandMainView(QMainWindow):

	def __init__(self):
		super().__init__()

		#setting up base window
		self.setWindowTitle('Randomizer')
		self.setFixedSize(700, 900)

		#setting up tabs from the TabWidget class
		self.table_widget = TabWidget.TabWidget(self)
		self.setCentralWidget(self.table_widget)

		self.show()

