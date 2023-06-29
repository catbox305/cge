__version__ = '0.7.1'

def clear():
	'''Clears the screen.\n\nCongrats, you somehow managed to avoid finding ext.clear and found ext.clear.clear instead!'''
	print('\033[2J')
	print('\033[0;0H')
