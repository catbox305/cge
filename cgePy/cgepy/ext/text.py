__version__ = '0.6.6'

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

class _container:
	pass

class container:
	def __init__(self):
		self = _container
	def empty(self):
		self = _container()

class Engine:
	def __init__(self, grid: Grid):
		self.grid = grid
		self.bin = container()
		self.temp = container()
	def Insert(self, index, content):
		self.temp.content = content
		self.temp.contentlen = len(content)-1

