try:
	from cgePy.cgepy import codes
except ModuleNotFoundError:
	try:
		from cgepy.cgepy import codes
	except ModuleNotFoundError:
		from cgepy import codes
BG = codes.BLUE #Background color
SC = codes.RED #Player color
GS = 100 #Size of grid