__version__ = '0.6.3'
try:
	from cgePy.cgepy.codes import *
	from cgePy.cgepy import cust
except ModuleNotFoundError:
	try:
		from cgepy.cgepy.codes import *
		from cgepy.cgepy import cust
	except ModuleNotFoundError:
		from cgepy.codes import *
		from cgepy import cust

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

class cge:
	class Exceptions:
		class OutOfRangeError(Exception):
			pass
		class MapError(Exception):
			pass
	class legacy:
		def cleargrid():
			counter=0
			newmap=[]
			for i in range(gridsize):
				newmap.append(background+"  ")
			return newmap
			
		def creategrid(size):
			update()
			newmap=[]
			for i in range(size):
				newmap.append(background+"  ")
			return newmap
		def updategrid(grid=""):
			cs()
			if grid != "":
				cm = grid
				grid = cm
			if grid == "":
				raise cge.Exceptions.OutOfRangeError("Grid index out of range:\nYou cannot update an empty grid.")
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
		def updatepos(newpos):
			global currentlyin
			try:
				cm[currentlyin] = background+"  "
			except IndexError:
				pass
			currentlyin = newpos
		def movepos(direction):
			global currentlyin
			try:
				cm[gridsize] = background+"  "
			except IndexError:
				pass
			if direction == "up":
				currentlyin-=pr
			if direction == "down":
				currentlyin+=pr
			if direction == "left":
				currentlyin-=1
			if direction == "right":
				currentlyin+=1
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
	def __init__(self, ctx=False):
        if  
		self.ctx = ctx
		self.sprites = []
        self.size = int(size)
		if ctx == False:
			self.ctx = cge.legacy.creategrid();
		else:
			if type(ctx) == list():
				self.ctx = new
			elif type(ctz) == Grid:
				self.ctx = new.ctx
			else:
				try:
					self.ctx = new.main
				except AttributeError:
					self.ctx = new

	def clear(self):

		self.ctx = cge.legacy.creategrid()
		
	def write(self, pos, new):
		try:
			self.ctx[pos] = new

		except IndexError:
			pass
			raise cge.Exceptions.OutOfRangeError
			
	def swap(self, new):
		self.ctx = new

	def Update(self):
		update()

		if self.sprites != []:

			self.temp = self.ctx.copy()

			for sprite in self.sprites:

				self.temp[sprite.pos] = sprite.sprite

			cge.legacy.updategrid(self.temp)

			del self.temp

		else:

			cge.legacy.updategrid(self.ctx)
			
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
			raise cge.Exceptions.MapError("Cannot paint an undefined map.")
		else:
			self.ctx = cge.legacy.paint(self.main)
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

class MainSprite:
	def __init__(self):
		spritecolor = RED
	def Color(self,color):
		spritecolor = color
	def Move(self,dir):
		if dir.lower() == "up":
			cge.legacy.movepos("up")
		if dir.lower() == "down":
			cge.legacy.movepos("down")
		if dir.lower() == "left":
			cge.legacy.movepos("left")
		if dir.lower() == "right":
			cge.legacy.movepos("right")
	def Drop(self,grid,request=False):
		if request == False:
			grid.sprites.append(self)
		if request == True:
			grid.sprites.remove(self)
			self.Drop(grid)
	def Remove(self,grid):
		grid.sprites.remove(self)
MainSprite1 = MainSprite()
del MainSprite
MainSprite = MainSprite1
del MainSprite1