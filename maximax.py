import time
import startingPositions

## TODO: Implementation of minimax algorithm

def potential_moves(block, gameboard):
	top = [-1]*10
	count = 0
	ans = []
	for row in range(20):
		for column in range(10):
			if top[column] == -1 and gameboard[row][column] != 'E':
				top[column] = row
				count = count + 1
			elif top[column] == -1 and row == 19:
				top[column] = 20
				count = count + 1
            
			if count == 10:
				break
		if count == 10:
			break
	for column in range(10):
		row = top[column]
		if block == 'I': #left -> right OR bottom -> top
			if column < 7:
				highest = min(top[column], top[column+1], top[column+2], top[column+3])
				if highest > 0:
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					temp.append((highest-1, column+2))
					temp.append((highest-1, column+3))
					ans.append(temp)
			if row > 3:
				temp = []
				temp.append((row-1, column))
				temp.append((row-2, column))
				temp.append((row-3, column))
				temp.append((row-4, column))
				ans.append(temp)

		elif block == 'J': # left-top -> right OR bottom -> top-right OR
			if column < 8: # left -> right-bottom OR bottom-left -> top
				highest = min(top[column], top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					temp.append((highest-1, column+2))
					ans.append(temp)
				highest = min(top[column]+1, top[column+1]+1, top[column+2])
				if highest > 1: # case 3
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-2, column+2))
					temp.append((highest-1, column+2))
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1]+2)
				if highest > 2: # case 2
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-2, column))
					temp.append((highest-3, column))
					temp.append((highest-3, column+1))
					ans.append(temp)
				highest = min(top[column], top[column+1])
				if highest > 2: # case 4
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					temp.append((highest-2, column+1))
					temp.append((highest-3, column+1))
					ans.append(temp)

		elif block == 'L': # left -> right-top OR top -> bottom-right OR
			if column < 8: # left-bottom -> right OR top-left -> bottom
				highest = min(top[column], top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					temp.append((highest-1, column+2))
					temp.append((highest-2, column+2))
					ans.append(temp)
				highest = min(top[column], top[column+1]+1, top[column+2]+1)
				if highest > 1: # case 3
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-2, column+2))
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1])
				if highest > 2: # case 2
					temp = []
					temp.append((highest-3, column))
					temp.append((highest-2, column))
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					ans.append(temp)
				highest = min(top[column]+2, top[column+1])
				if highest > 2: # case 4
					temp = []
					temp.append((highest-3, column))
					temp.append((highest-3, column+1))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column+1))
					ans.append(temp)

		elif block == 'O': # left-top -> right-top -> left-bottom -> right-bottom
			if column < 9:
				highest = min(top[column], top[column+1])
				if highest > 1:
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					ans.append(temp)

		elif block == 'S': # left -> right OR top -> bottom
			if column < 8: 
				highest = min(top[column], top[column+1], top[column+2]+1)
				if highest > 1: # case 1
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					temp.append((highest-2, column+1))
					temp.append((highest-2, column+2))
					ans.append(temp)
			if column < 9: 
				highest = min(top[column]+1, top[column+1])
				if highest > 2: # case 3
					temp = []
					temp.append((highest-3, column))
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column+1))
					ans.append(temp)

		elif block == 'T': # left -> right -> top OR top -> bottom -> right OR
			if column < 8: # left -> right -> bottom OR -> left -> top -> bottom
				highest = min(top[column], top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					temp.append((highest-1, column+2))
					temp.append((highest-2, column+1))
					ans.append(temp)
				highest = min(top[column]+1, top[column+1], top[column+2]+1)
				if highest > 1: # case 3
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-2, column+2))
					temp.append((highest-1, column+1))
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1]+1)
				if highest > 2: # case 2
					temp = []
					temp.append((highest-3, column))
					temp.append((highest-2, column))
					temp.append((highest-1, column))
					temp.append((highest-2, column+1))
					ans.append(temp)
				highest = min(top[column]+1, top[column+1])
				if highest > 2: # case 4
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-3, column+1))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column+1))
					ans.append(temp)

		elif block == 'Z': # left -> right OR bottom -> top
			if column < 8: 
				highest = min(top[column]+1, top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column+1))
					temp.append((highest-1, column+2))
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1]+1)
				if highest > 2: # case 2
					temp = []
					temp.append((highest-1, column))
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-3, column+1))
					ans.append(temp)
	return ans


def get_moves(coord, gameboard, block):
	ans = []
	x = 3
	if block == 'I': 
		if (coord[0][1] == coord[1][1]):
			ans.append('up')
			x = 5
		
	elif block == 'J': 
		if (coord[0][0] - 1 == coord[1][0]):
			ans.append('up')
			x = 4
		elif (coord[2][0] + 1 == coord[3][0]):
			ans.append('up')
			ans.append('up')
		elif (coord[2][0] - 1 == coord[3][0]):
			ans.append('up')
			ans.append('up')
			ans.append('up')

	elif block == 'L': 
		if (coord[0][0] + 1 == coord[1][0]):
			ans.append('up')
			x = 4
		elif (coord[0][0] - 1 == coord[1][0]):
			ans.append('up')
			ans.append('up')
		elif (coord[2][0] + 1 == coord[3][0]):
			ans.append('up')
			ans.append('up')
			ans.append('up')

	elif block == 'S': 
		if (coord[0][1] == coord[1][1]):
			ans.append('up')
			x = 4

	elif block == 'T': 
		if (coord[1][1] + 1 == coord[3][1]):
			ans.append('up')
			x = 4
		elif (coord[1][0] + 1 == coord[3][0]):
			ans.append('up')
			ans.append('up')
		elif (coord[1][0] + 2 == coord[3][0]):
			ans.append('up')
			ans.append('up')
			ans.append('up')
		
	elif block == 'Z': 
		if (coord[0][1] == coord[1][1]):
			ans.append('up')
			x = 4

	elif block == 'O':
		x = 4

	for i in range(x, coord[0][1]):
		ans.append('right')
	for i in range(coord[0][1], x):
		ans.append('left')
	return ans
		



