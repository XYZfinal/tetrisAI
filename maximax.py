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

		elif block == "J":
			if column < 8: 
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

		elif block == "L":
			if column < 8: 
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

		elif block == "O":
			if column < 9:
				highest = min(top[column], top[column+1])
				if highest > 1:
					temp = []
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column))
					temp.append((highest-1, column+1))
					ans.append(temp)

		elif block == "S":
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

		elif block == "T":
			if column < 8: 
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

		elif block == "Z":
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
				if highest > 2: # case 3
					temp = []
					temp.append((highest-3, column))
					temp.append((highest-2, column))
					temp.append((highest-2, column+1))
					temp.append((highest-1, column+1))
					ans.append(temp)
	return ans
