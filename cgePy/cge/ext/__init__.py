__version__ = '0.7.3'

def clear():
	'''Clears the screen.'''
	print('\033[0;0H',end='')
	print('\033[2J',end='')
