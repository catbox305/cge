__version__ = "0.7.3"
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