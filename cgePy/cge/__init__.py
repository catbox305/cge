__version__ = '0.7.1'
try:
	from cgepy.cge.colors import *
except ModuleNotFoundError:
	try:
		from cgePy.cge.colors import *
	except ModuleNotFoundError:
		from cge.colors import *

def cs(): #clear-screen
	'''Use cge.ext.clear instead!\n\nClears the screen.'''
	print("\033[2J") #Clears screen
	print('\033[0;0H') #Resets cursor

spritecolor = RED
background = BLUE
gridsize = 100

global pr

class from_getkey:
	'''These escape sequences were taken from the getkey module. I didn't find them!'''
	def __init__(self):
		up = "\x1b[A"
		down = "\x1b[B"
		right = "\x1b[C"
		left = "\x1b[D"

keys = from_getkey()
del from_getkey

def update():
	global pr
	pr = int(gridsize**0.5)

update()

"Classes"

class Output:
	pass
""
class Exceptions:
	class OutOfRangeError(Exception):
		pass
	class MapError(Exception):
		pass
""
class legacy:
	'''Legacy functions previously used instead of classes.\n\nNote:\nThese functions are still in use. However, they are considered legacy as you do not need to manually call them anymore.'''

	def creategrid() -> list:
		'''Returns an empty grid.'''
		newmap=[]
		for i in range(gridsize):
			newmap.append(background+"  ")
		return newmap
		
	def updategrid(grid):
		'''Print a grid onto the screen'''
		buffer = []
		for n in range(len(grid)):
			buffer.append(grid[n])
			if (n+1) % pr == 0:
				buffer.append("\n")
		cs()
		print(''.join(buffer), end='')
		print("\x1b[0m")
		
	def paint(map: str) -> list:
		'''Paint a grid using text.'''
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
""
class Grid:

	def __init__(self, ctx="", border = False):
		update()
		self.ctx = ctx
		self.sprites = []

		if ctx == "":
			if border == False:
				self.ctx = legacy.creategrid()
			elif type(border) == str:
				self.ctx = legacy.creategrid()
				for n in range(len(self.ctx)):
					if n <= pr-1:
						self.ctx[n] = border
					elif n > pr-1 and n < gridsize-pr:
						if n % pr == 0 or (n+1) % pr == 0:
							self.ctx[n] = border
					if n >= gridsize-pr:
						self.ctx[n] = border
						
				
		else:

			if type(ctx) == list:
				self.ctx = new
			elif type(ctx) == Grid:
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
""		     
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
""
class Sprite:
	def __init__(self,pos=0,color=RED):
		self.pos = pos
		self.color = color
		self.sprite = color+"  "
	def Color(self,color):
		self.color = color
		self.sprite = color+"  "
	def Move(self,dir):
		if dir.lower() in ["up","w","i","\x1b[A"]:
			self.pos -= pr
		if dir.lower() in ["down","s","k","\x1b[B"]:
			self.pos += pr
		if dir.lower() in ["left","a","j","\x1b[D"]:
			self.pos -= 1
		if dir.lower() in ["right","d","l","\x1b[C"]:
			self.pos += 1

	def Drop(self,grid,request=False):
		if request == False:
			grid.sprites.append(self)
		if request == True:
			grid.sprites.remove(self)
			self.Drop(grid)
	def Remove(self,grid):
		grid.sprites.remove(self)
