__version__ = '0.7.2'

def clear():
	'''Clears the screen.'''
	print('\033[2J')
	print('\033[0;0H')