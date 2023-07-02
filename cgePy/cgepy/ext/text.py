__version__ = '0.7.1'

try:
	from cgePy.cgepy.colors import *
	from cgePy.cgepy.__init__ import *
except ModuleNotFoundError:
	try:
		from cgepy.cgepy.colors import *
		from cgepy.cgepy.__init__ import *
	except ModuleNotFoundError:
		from cgepy.colors import *
		from cgepy.__init__ import *

class empty:
	'''The name says it all.'''
	pass

class TextEngine:
	'''A text engine allowing for text inside grids.'''
	def __init__(self, grid: Grid) -> TextEngine:
		self.grid = grid
		self.temp = empty()
	def Insert(self, content, index=0):
		self.temp.content = content
		self.index = index
		self.temp.contentlen = len(content)
		if self.temp.contentlen % 2 != 0:
			self.temp.content += " "
			self.temp.contentlen += 1
		self.n = 0
		self.temp.content = list(self.temp.content)
		self.temp.ready = []
		for i in range(0, len(self.temp.content), 2): #https://stackoverflow.com/a/312464/20800465
			self.temp.ready.append(self.temp.content[i:i + 2]) #https://stackoverflow.com/a/312464/20800465
		print(self.temp.ready)
		for i in self.temp.ready:
			self.grid.ctx[self.index + self.n] = self.grid.ctx[self.index + self.n].replace(self.grid.ctx[self.index + self.n][len(self.grid.ctx[self.index + self.n]) - 2:],"".join(i)) #https://www.knowprogram.com/python/python-replace-last-two-characters-in-string/
			self.n+=1