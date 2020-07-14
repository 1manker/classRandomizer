#Randomizer.py
#Author: Lucas Manker
#Class randomizer

import sys
import RandMainView as rmv
from PyQt5.QtWidgets import QApplication

__version__ = '0.1'
__author__ = 'Lucas Manker'

def main():
	randomizer = QApplication(sys.argv)
	view = rmv.RandMainView()
	view.show()
	sys.exit(randomizer.exec_())

if __name__ == '__main__':
	main()