import time
import startingPositions

## TODO: Implementation of minimax algorithm

def potential_moves(block, gameboard):
	top = [-1]*10
	count = 0
	ans = []
	temp = gameboard
	for row in range(20):
	for column in range(10):
		if top[column] == -1 and gameboard[row][column] != 'E':
		top[column] = row
		count = count + 1
	    if count == 10:
		break
	if count == 10:
		break

	for column in range(10):
		row = top[column]
		if block == 'I':
			if column < 7:
				highest = min(top[column], top[column+1], top[column+2], top[column+3])
				if highest > 0:
					temp = gameboard
					temp[highest-1][column] = 'I'
					temp[highest-1][column+1] = 'I'
					temp[highest-1][column+2] = 'I'
					temp[highest-1][column+3] = 'I'
					ans.append(temp)
			if row > 3:
				temp = gameboard
				temp[row-1][column] = 'I'
				temp[row-2][column] = 'I'
				temp[row-3][column] = 'I'
				temp[row-4][column] = 'I'
				ans.append(temp)

		elif block == "J":
			if column < 8: 
				highest = min(top[column], top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = gameboard
					temp[highest-2][column] = 'J'
					temp[highest-1][column] = 'J'
					temp[highest-1][column+1] = 'J'
					temp[highest-1][column+2] = 'J'
					ans.append(temp)
				highest = min(top[column]+1, top[column+1]+1, top[column+2])
				if highest > 1: # case 3
					temp = gameboard
					temp[highest-2][column] = 'J'
					temp[highest-2][column+1] = 'J'
					temp[highest-2][column+2] = 'J'
					temp[highest-1][column+2] = 'J'
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1]+2)
				if highest > 2: # case 2
					temp = gameboard
					temp[highest-1][column] = 'J'
					temp[highest-2][column] = 'J'
					temp[highest-3][column] = 'J'
					temp[highest-3][column+1] = 'J'
					ans.append(temp)
				highest = min(top[column], top[column+1])
				if highest > 2: # case 4
					temp = gameboard
					temp[highest-1][column] = 'J'
					temp[highest-1][column+1] = 'J'
					temp[highest-2][column+1] = 'J'
					temp[highest-3][column+1] = 'J'
					ans.append(temp)

		elif block == "L":
			if column < 8: 
				highest = min(top[column], top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = gameboard
					temp[highest-1][column] = 'L'
					temp[highest-1][column+1] = 'L'
					temp[highest-1][column+2] = 'L'
					temp[highest-2][column+2] = 'L'
					ans.append(temp)
				highest = min(top[column], top[column+1]+1, top[column+2]+1)
				if highest > 1: # case 3
					temp = gameboard
					temp[highest-1][column] = 'L'
					temp[highest-2][column] = 'L'
					temp[highest-2][column+1] = 'L'
					temp[highest-2][column+2] = 'L'
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1])
				if highest > 2: # case 2
					temp = gameboard
					temp[highest-3][column] = 'L'
					temp[highest-2][column] = 'L'
					temp[highest-1][column] = 'L'
					temp[highest-1][column+1] = 'L'
					ans.append(temp)
				highest = min(top[column]+2, top[column+1])
				if highest > 2: # case 4
					temp = gameboard
					temp[highest-3][column] = 'L'
					temp[highest-3][column+1] = 'L'
					temp[highest-2][column+1] = 'L'
					temp[highest-1][column+1] = 'L'
					ans.append(temp)

		elif block == "O":
			if column < 9:
				highest = min(top[column], top[column+1])
				if highest > 1:
					temp = gameboard
					temp[highest-2][column] = 'O'
					temp[highest-2][column+1] = 'O'
					temp[highest-1][column] = 'O'
					temp[highest-1][column+1] = 'O'
					ans.append(temp)

		elif block == "S":
			if column < 8: 
				highest = min(top[column], top[column+1], top[column+2]+1)
				if highest > 1: # case 1
					temp = gameboard
					temp[highest-1][column] = 'S'
					temp[highest-1][column+1] = 'S'
					temp[highest-2][column+1] = 'S'
					temp[highest-2][column+2] = 'S'
					ans.append(temp)
			if column < 9: 
				highest = min(top[column]+1, top[column+1])
				if highest > 2: # case 3
					temp = gameboard
					temp[highest-3][column] = 'S'
					temp[highest-2][column] = 'S'
					temp[highest-2][column+1] = 'S'
					temp[highest-1][column+1] = 'S'
					ans.append(temp)

		elif block == "T":
			if column < 8: 
				highest = min(top[column], top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = gameboard
					temp[highest-1][column] = 'T'
					temp[highest-1][column+1] = 'T'
					temp[highest-1][column+2] = 'T'
					temp[highest-2][column+1] = 'T'
					ans.append(temp)
				highest = min(top[column]+1, top[column+1], top[column+2]+1)
				if highest > 1: # case 3
					temp = gameboard
					temp[highest-2][column] = 'T'
					temp[highest-2][column+1] = 'T'
					temp[highest-2][column+2] = 'T'
					temp[highest-1][column+1] = 'T'
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1]+1)
				if highest > 2: # case 2
					temp = gameboard
					temp[highest-3][column] = 'T'
					temp[highest-2][column] = 'T'
					temp[highest-1][column] = 'T'
					temp[highest-2][column+1] = 'T'
					ans.append(temp)
				highest = min(top[column]+1, top[column+1])
				if highest > 2: # case 4
					temp = gameboard
					temp[highest-2][column] = 'T'
					temp[highest-3][column+1] = 'T'
					temp[highest-2][column+1] = 'T'
					temp[highest-1][column+1] = 'T'
					ans.append(temp)

		elif block == "Z":
			if column < 8: 
				highest = min(top[column]+1, top[column+1], top[column+2])
				if highest > 1: # case 1
					temp = gameboard
					temp[highest-2][column] = 'Z'
					temp[highest-2][column+1] = 'Z'
					temp[highest-1][column+1] = 'Z'
					temp[highest-1][column+2] = 'Z'
					ans.append(temp)
			if column < 9: 
				highest = min(top[column], top[column+1]+1)
				if highest > 2: # case 3
					temp = gameboard
					temp[highest-3][column] = 'Z'
					temp[highest-2][column] = 'Z'
					temp[highest-2][column+1] = 'Z'
					temp[highest-1][column+1] = 'Z'
					ans.append(temp)

	return ans
