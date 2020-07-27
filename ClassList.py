#ClassList.py
#Lucas Manker
#Class which manages class lists

from collections import Counter

class ClassList():
	def __init__(self):
		self.names = []
		self.ids = {}
		self.genders = {}

	def getGenderSplit(self):
		ret = Counter(self.genders.values())
		males = ret['M']
		females = ret['F']
		return ("There are %s males, and %s females" % (males, females))

	def importList(self, file):
		f = open(file, "r")
		lines = f.readlines()
		for line in lines:
			entries = line.split(',')
			entry = entries[0] + ',' + entries[1]
			self.names.append(entry)
			self.ids[entry] = entries[3].strip()
			self.genders[entry] = entries[2].strip()
		print(self.genders)
