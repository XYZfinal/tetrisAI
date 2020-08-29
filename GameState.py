import pyautogui
import blockColors as bc

## TODO: Implementation of Game state construction
###  Analysis of screenshot into game state object for minimax algorithm

def checkBlock(rgb):
	if rgb == bc.EMPTY:
		return 'EMPTY'
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
		return 'EMPTY'
		#return 'S_SHADOW'
	elif rgb == bc.Z_BLOCK_SHADOW:
		return 'EMPTY'
		#return 'Z_SHADOW'
	elif rgb == bc.L_BLOCK_SHADOW:
		return 'EMPTY'
		#return 'L_SHADOW'
	elif rgb == bc.J_BLOCK_SHADOW:
		return 'EMPTY'
		#return 'J_SHADOW'
	elif rgb == bc.O_BLOCK_SHADOW:
		return 'EMPTY'
		#return 'O_SHADOW'
	elif rgb == bc.I_BLOCK_SHADOW:
		return 'EMPTY'
		#return 'I_SHADOW'
	elif rgb == bc.T_BLOCK_SHADOW:
		return 'EMPTY'
		#return 'T_SHADOW'
	else:
		#Should never happen
		return str(rgb)
	

class GameState:
	def __init__(self, image):
		self.matrix = [['EMPTY','EMPTY','EMPTY','EMPTY','EMPTY','EMPTY','EMPTY','EMPTY','EMPTY','EMPTY']]
		for i in range(1, 20):
			y = i * 24 + 12
			row = []
			for j in range(10):
				x = j * 24 + 12
				pix = image.getpixel((x, y))
				blockContent = checkBlock(pix)
				row.append(blockContent)
			self.matrix.append(row)

