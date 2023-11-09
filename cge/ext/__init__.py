__version__ = '1.0.0-pre.1'

def clear():
	'''Clears the screen.'''
	print('\033[0;0H',end='')
	print('\033[2J',end='')
