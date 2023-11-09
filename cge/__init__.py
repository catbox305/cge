__version__ = "0.7.3"

# Import required modules

from colors import Presets
from _partial import out
from _exceptions import Exceptions
from ext import clear

# Initialize settings

spritecolor = Presets.red()
background = Presets.blue()

# Classes

class Grid:

	def __init__(self, size:int = 20):
		self.sprites = []
		self.size = size

		self.ctx = [[background for i in range(self.size)] for i in range(self.size)]


	def Clear(self):
		"""Clears the grid context. Does not erase sprites."""
		self.ctx = [[background for i in range(self.size)] for i in range(self.size)]
		
	def Write(self, pos, new):
		"""Change the color value of a position on the grid."""
		try:
			self.ctx[pos[1][0]] = new

		except IndexError:
			e = "Grid index out of range"
			raise Exceptions.GridError(e)
	def w(self, pos, new):
		"""Change the color value of a position on the grid."""
		try:
			self.ctx[pos[1][0]] = new

		except IndexError:
			e = "Grid index out of range"
			raise Exceptions.GridError(e)

	def Update(self, screenclearing = True):
		"""Prints the grid to the screen using a buffer."""
		if self.sprites != []:
			tmp = self.ctx.copy()

			for sprite in self.sprites:
				tmp[sprite.pos[1]][sprite.pos[0]] = sprite.color

			out(tmp, screenclearing)

		else:
			out(self.ctx, screenclearing)  

class Sprite:

	def __init__(self, pos = (0,0), color = spritecolor):
		self.pos = pos
		self.color = color

	def Move(self, dir:str):
		if dir.lower() in ["up","w","i","\x1b[A","north"]:
			self.pos[1] -= 1
		if dir.lower() in ["down","s","k","\x1b[B","south"]:
			self.pos[1] += 1
		if dir.lower() in ["left","a","j","\x1b[D","west"]:
			self.pos[0] -= 1
		if dir.lower() in ["right","d","l","\x1b[C","east"]:
			self.pos[0] += 1

	def Go(self, pos = (0,0)):
		self.pos = pos

	def Drop(self, grid):
		grid.sprites.append(self)
	def Remove(self, grid):
		grid.sprites.remove(self)