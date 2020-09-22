import pyautogui
import blockColors as bc
import debug

## TODO: Implementation of Game state construction
###  Analysis of screenshot into game state object for minimax algorithm

def checkBlock(rgb):
	if rgb == bc.EMPTY:
		return 'E'
	elif rgb == bc.S_BLOCK:
		return 'S'
	elif rgb == bc.Z_BLOCK:
		return 'Z'
	elif rgb == bc.L_BLOCK:
		return 'L'
	elif rgb == bc.J_BLOCK:
		return 'J'
	elif rgb == bc.O_BLOCK:
		return 'O'
	elif rgb == bc.I_BLOCK:
		return 'I'
	elif rgb == bc.T_BLOCK:
		return 'T'
	elif rgb == bc.S_BLOCK_SHADOW:
		return 'E'
		#return 'S_SHADOW'
	elif rgb == bc.Z_BLOCK_SHADOW:
		return 'E'
		#return 'Z_SHADOW'
	elif rgb == bc.L_BLOCK_SHADOW:
		return 'E'
		#return 'L_SHADOW'
	elif rgb == bc.J_BLOCK_SHADOW:
		return 'E'
		#return 'J_SHADOW'
	elif rgb == bc.O_BLOCK_SHADOW:
		return 'E'
		#return 'O_SHADOW'
	elif rgb == bc.I_BLOCK_SHADOW:
		return 'E'
		#return 'I_SHADOW'
	elif rgb == bc.T_BLOCK_SHADOW:
		return 'E'
		#return 'T_SHADOW'
	else:
		#Should never happen
		return 'E'
	

class GameState:
	def __init__(self, gameImg, forsightImg, holdImg, square):
		# Processes the screenshot image of the current game state and transforms it into all necessary information for the AI
		## Create matrix of current game board
		self.matrix = [['E','E','E','E','E','E','E','E','E','E']]
		for i in range(1, 20):
			y = i * square + square*0.5
			row = []
			for j in range(10):
				x = j * square + square*0.5
				pix = gameImg.getpixel((x, y))
				blockContent = checkBlock(pix)
				row.append(blockContent)
			self.matrix.append(row)

		## Determine the next block to place
		self.next = checkBlock(gameImg.getpixel((square*4.5, square*0.5)))

		## Determine the holded block
		hold1 = checkBlock(holdImg.getpixel((square*1.5, square*0.5)))
		hold2 = checkBlock(holdImg.getpixel((square*1.5, square*1.5)))
		if hold1 != 'E':
			self.hold = hold1
		else:
			self.hold = hold2

		## Determine the next blocks in the future
		self.future = []
		for i in range(5):
			block1 = checkBlock(forsightImg.getpixel((square*1.5 , i*3*square + square*0.5)))
			block2 = checkBlock(forsightImg.getpixel((square*1.5 , i*3*square + square*1.5)))
			if block1 != 'E':
				self.future.append(block1)
			else:
				self.future.append(block2)

	def debug_pretty_print(self):
		## Print future block in line
		for block in self.future:
			print('Future blocks: ' + block)

		## Print held block
		print('\nHeld block: ' + self.hold + '\n')

		## Print current block to place
		print('Block to place: ' + self.next + '\n')

		## Print current game board
		debug.print_matrix(self.matrix)


