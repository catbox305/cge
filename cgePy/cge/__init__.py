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

class keys:
	"""Arrow key escape sequences."""
	up = "\x1b[A"
	down = "\x1b[B"
	right = "\x1b[C"
	left = "\x1b[D"


class legacy:
	"""Deprecated functions deployed by the library before release 0.7.3\nWarning: This class will be dropped by release 0.7.5"""

	def creategrid() -> list:
		"""Returns an empty grid context."""
		newmap=[]
		for i in range(int(gridsize)):
			newmap.append(background+"  ")
		return newmap
		
	def updategrid(grid):
		"""Print a grid context onto the screen."""
		buffer = []
		for n in range(len(grid)):
			buffer.append(grid[n])
			if (n+1) % pr == 0:
				buffer.append("\n")
		clear()
		print(''.join(buffer), end='')
		print("\x1b[0m")
		
	def paint(map: str) -> list:
		"""Paint a grid context using text."""
		map = map.replace(" ","")
		map = map.replace(",","")
		map = map.replace("\n","")
		map = map.replace("BG",background+"  ,")
		map = map.replace("RE",RED+"  ,")
		map = map.replace("YE",YELLOW+"  ,")
		map = map.replace("GR",GREEN+"  ,")
		map = map.replace("BL",BLUE+"  ,")
		map = map.replace("CY",CYAN+" ,")
		map = map.replace("MA",MAGENTA+"  ,")
		map = map.replace("BB",BLACK+"  ,")
		map = map.replace("WH",WHITE+"  ,")
		map = map.replace("RR",RESET+"  ,")
		map = map.split(",")
		return map

class Grid:

	def __init__(self, size:int = 20):
		self.sprites = []

		self.ctx = [[background for i in range(size)] for i in range(size)]


	def Clear(self):
		"""Clears the grid context. Does not erase sprites."""
		self.ctx = [[background for i in range(size)] for i in range(size)]
		
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

	def Update(self, clean = True):
		"""Prints the grid to the screen using a buffer.\n\nPassing the argument 'false' will disable automatic screen clearing."""
		if self.sprites != []:
			tmp = self.ctx.copy()

			for sprite in self.sprites:
				tmp[sprite.pos[1]][sprite.pos[0]] = sprite.color

			out(tmp)

		else:
			out(self.ctx, clean)  

#class Map:
#
#
#	def __init__(self, map=False):
#		if map==False:
#			self.ctx = '''null'''
#		else:
#			self.ctx = map
#	def Paint(self):
#		if self.ctx == '''null''':
#			raise Exceptions.MapError("Cannot paint an undefined map.")
#		else:
#			self.ctx = legacy.paint(self.ctx)
#			del self.ctx
# 			self.__class__ = Grid

class Sprite:

	def __init__(self, pos = (0,0), color = spritecolor):
		self.pos = pos
		self.color = color

	def Move(self, dir:str):
		if dir.lower() in ["up","w","i","\x1b[A"]:
			self.pos[1] -= 1
		if dir.lower() in ["down","s","k","\x1b[B"]:
			self.pos[1] += 1
		if dir.lower() in ["left","a","j","\x1b[D"]:
			self.pos[0] -= 1
		if dir.lower() in ["right","d","l","\x1b[C"]:
			self.pos[0] += 1

	def Go(self, pos = (0,0)):
		self.pos = pos

	def Drop(self, grid):
		grid.sprites.append(self)
	def Remove(self, grid):
		grid.sprites.remove(self)