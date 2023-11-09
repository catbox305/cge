class Color:
	'''Takes an RGB sequence and converts it into both a background color and text color.\n\nArguments:\n\tr-int, g-int, b-int\nReturns:\n\tA color object.'''
	def __init__(self, r:int, g:int, b:int):

		if (r > 255) or (g > 255) or (b > 255): # Raise exception if an RGB value exceeds 255
			raise Exception("RGB values cannot exceed 255")

		self.r = str(r)
		self.g = str(g)
		self.b = str(b)
		self.background = f"\033[48;2;{r};{g};{b}m"
		self.fore = f"\033[38;2;{r};{g};{b}m"
	

class Presets:
	def black(): return Color(0,0,0)
	def red(): return Color(200,0,0)
	def yellow(): return Color(200,200,0)
	def green(): return Color(0,200,0)
	def blue(): return Color(0,0,200)
	def magenta(): return Color(200,0,200)
	def white(): return Color(200,200,200)