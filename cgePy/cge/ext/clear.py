__version__ = '0.7.1'

def clear():
	'''Clears the screen.\n\nCongrats, you somehow managed to avoid using ext.clear!\n(Now you are using ext.clear.clear)'''
	print('\033[2J')
	print('\033[0;0H')
