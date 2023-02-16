__version__ = '0.1.0'

import cgepy as cge

class Page():
	def __init__(self,contents):
		self.contents = contents
		self.main = cge.Grid(self.contents)
	def Update(self):
		self.main.Update()
		

class Notebook():
	def __init__(self,name,author=""):
		self.name = name
		self.author = author
		self.pages = [name+"\nby "+author]
	def Add(self,page):
		self.pages.append(page)
	def Update(self,page):
		if type(page) == int:
			if page != 1:
				self.pages[page-1].Update()
			else:
				print(self.pages[0])
		elif type(page) == Page:
			if page in self.pages:
				page.Update()
			else:
				raise KeyError