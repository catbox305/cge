__version__ = '0.7.0'

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
	pass

class Engine:
	def __init__(self, grid: Grid):
		self.grid = grid
		self.temp = empty()
	def Insert(self, content, index):
		self.temp.content = content
		self.index = index
		self.temp.contentlen = len(content)
		if self.temp.contentlen % 2 != 0:
			self.temp.content += "  "
			self.temp.contentlen += 1
		self.n = 0
		self.temp.content = list(self.temp.content)
		self.temp.ready = []
		for i in range(0, len(self.temp.content), 2):
			self.temp.ready.append(self.temp.content[i:i + n])
		for i in self.temp.ready:
			self.grid[n] = self.grid[n].replace("  ",i)
			n+=1



e = Grid()
b = Engine(e)
b.Insert("12345",3)
e.Update()
