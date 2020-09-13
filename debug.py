import copy

def print_matrix(matrix):
	for row in matrix:
		toPrint = ''
		for cell in row:
			toPrint += cell
		print(toPrint)

def print_coords(coords, matrix):
	result = ''
	tempMatrix = copy.deepcopy(matrix)
	for i in range(4):
		temp = str(i+1) + 'th coordinates: x is ' + str(coords[i][0]) + ', y is ' + str(coords[i][1])
		result += temp + '\n'
		tempMatrix[coords[i][0]][coords[i][1]] = 'N'
	print_matrix(tempMatrix)
	result += '\n'
	print(result)
