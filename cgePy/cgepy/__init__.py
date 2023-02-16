__version__ = '0.6.4'
try:
	from cgePy.cgepy.colors import *
except ModuleNotFoundError:
	try:
		from cgepy.cgepy.colors import *
	except ModuleNotFoundError:
		from cgepy.colors import *

import time

def cs():
	print("\033[2J")
	print("\033[H")

spritecolor = RED
background = BLUE
gridsize = 100

currentlyin = 0
gridinfo = {}
global pr

def update():
	global pr
	pr = int(gridsize**0.5)

update()



class Exceptions:
	class OutOfRangeError(Exception):
		pass
	class MapError(Exception):
		pass
class legacy:
	def creategrid():
			newmap=[]
			for i in range(gridsize):
				newmap.append(background+"  ")
			return newmap
	def updategrid(grid=""):
		cs()
		if grid != "":
			cm = grid
			grid = cm
		if grid == "":
			raise Exception
		counter=-1
		refr=-1
		cs()
		for i in range(0,gridsize):
			counter+=1
			refr+=1
			if refr == pr:
				if refr == gridsize-pr:
					refr = 1
					print("")
				else:
					print("")
					refr=0
			print(grid[counter], end="")
		print(white+"")
	def paint(map):
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
	def __init__(self, ctx="", new=True):
		self.ctx = ctx
		self.sprites = []
		if new == True:
			self.ctx = legacy.creategrid()
		else:
			if new == list():
				self.ctx = new
			elif new == Grid:
				self.ctx = new.ctx
			else:
				try:
					self.ctx = new.main
				except AttributeError:
					self.ctx = new

	def clear(self):

		self.ctx = legacy.creategrid()
		
	def write(self, pos, new):
		try:
			self.ctx[pos] = new

		except IndexError:
			pass
			raise Exceptions.OutOfRangeError
			
	def swap(self, new):
		self.ctx = new

	def Update(self):
		update()

		if self.sprites != []:

			self.temp = self.ctx.copy()

			for sprite in self.sprites:

				self.temp[sprite.pos] = sprite.sprite

			legacy.updategrid(self.temp)

			del self.temp

		else:

			legacy.updategrid(self.ctx)
			
	def Self(self):
		return self.ctx
class Map:
	def __init__(self, map=False):
		if map==False:
			self.main = '''undefined'''
		else:
			self.main = map
	def Paint(self):
		if self.main == '''undefined''':
			raise Exceptions.MapError("Cannot paint an undefined map.")
		else:
			self.ctx = legacy.paint(self.main)
			del self.main
			self.__class__ = Grid
class Sprite:
	def __init__(self,pos=0,color=RED):
		self.pos = pos
		self.color = color
		self.sprite = color+"  "
	def Color(self,color):
		self.color = color
		self.sprite = color+"  "
	def Move(self,dir):
		if dir.lower() in ["up","w","i"]:
			self.pos -= pr
		if dir.lower() in ["down","s","k"]:
			self.pos += pr
		if dir.lower() in ["left","a","j"]:
			self.pos -= 1
		if dir.lower() in ["right","d","l"]:
			self.pos += 1

	def Drop(self,grid,request=False):
		if request == False:
			grid.sprites.append(self)
		if request == True:
			grid.sprites.remove(self)
			self.Drop(grid)
	def Remove(self,grid):
		grid.sprites.remove(self)
