__version__ = "0.7.3"

def out(canvas, clean = True):
	"""Higher resolution canvas output using unicode half-blocks.\nNote that index zero of your canvas will define the length of all other indexes."""

	if clean == True:
		print('\033[0;0H',end='')
		print('\033[2J',end='')

	buffer = ""
	index_i = -2

	for i in range(len(canvas.ctx)//2):
		index_j = -1
		index_i += 2

		for j in range(len(canvas.ctx[0])):
			index_j += 1

			j = canvas.ctx[index_i][index_j].background + canvas.ctx[index_i+1][index_j].fore + '▄'
			buffer += j

		buffer += '\033[0m\n'

	print(buffer)