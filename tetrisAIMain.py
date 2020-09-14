import pyautogui
import time
import copy
import GameState as gs
import evaluate as ev
import maximax as algo
import debug

## DEBUG?
DEBUG = True

## Each square in the game has dimensions of 24*24 pixels. The are a total of 10*20 square in the game
LEFT = 0
TOP = 0
WIDTH = 240
HEIGHT = 480

## Calibrate top left corner for screenshots 
def calibrate():
	global LEFT
	global TOP
	leftUpCorner = pyautogui.locateOnScreen('leftUpCorner.JPG', confidence = 0.95)
	LEFT = leftUpCorner[0] + 1
	TOP = leftUpCorner[1] + 1

## Capture a screenshot of exactly the game board
def capture_game(name):
	image = pyautogui.screenshot(name, region=(LEFT, TOP, WIDTH, HEIGHT))
	return image

### Capture a screenshot of exactly the next blocks
def capture_forsight():
	image = pyautogui.screenshot('forsight.png', region=(LEFT+WIDTH+30, TOP+24, 24*4, 24*14))
	return image

### Capture holded block
def capture_hold():
	image = pyautogui.screenshot('hold.png', region=(LEFT-105, TOP+24, 24*4, 24*2))
	return image

### Capture all game info
def capture_inputs():
	gameImg = capture_game('game.png')
	forsightImg = capture_forsight()
	holdImg = capture_hold()
	return gameImg, forsightImg, holdImg

## Start new game by click new game button on jstris window and pressing f4
def initiate_game():
	# Finding new game button location
	newGameButtonLocation = pyautogui.locateOnScreen('newgamebutton.JPG', confidence = 0.9)
	newGameButtonCenterPoint = pyautogui.center(newGameButtonLocation)

	# Start game
	pyautogui.click(newGameButtonCenterPoint.x, newGameButtonCenterPoint.y)
	pyautogui.press('f4')

	## Wait 1.75 second for the game to start
	time.sleep(1.75)

## initiate the AI by sacking 1 game to calibrate the game (mainly just making sure the top left square is empty for screen print calibration)
## and initiate a second game for the ai to beat
def initiate():
	## Suicide 1 game, making sure the left top corner is untouched for screenprint calibration
	initiate_game()
	pyautogui.press('space', 20)
	calibrate()
	initiate_game()

## input a sequence of moves for the ai to accomplish, the goal is to place exactly one block by the end of the sequence 
## also screenprint for debugging
def do_moves(moves):
	pyautogui.press(moves)
	### dummy ai to test usability of pyautogui (TO REMOVE)
	pyautogui.press('shift')
	for i in range(5):
		pyautogui.press('left', presses=5)
		pyautogui.press('space')

	for i in range(5):
		pyautogui.press('right', presses=5)
		pyautogui.press('space')

	for i in range(3):
		pyautogui.press('space')

## check all potential moves and find the best move that beats the given maxscore
## return the same bestPotential and maxscore if nothing is better
def check_moves(bestPotential, maxScore, potential_moves, board):
	bestPotential = bestPotential
	maxScore = maxScore
	changed = False
	for i in range(len(potential_moves)):
		tempMatrix = copy.deepcopy(board)
		for xy in potential_moves[i]:
			tempMatrix[xy[0]][xy[1]] = 'N'
		score = ev.evaluate(tempMatrix)

		if DEBUG:
			debug.print_matrix(tempMatrix)
			print(str(score))

		if score > maxScore:
			maxScore = score
			bestPotential = i
			changed = True

	return bestPotential, maxScore, changed

## find best moves available for the AI at this point, factoring both the current block to place and the held piece
def find_best_move(holdPiece, nextPiece, board):
	potential_moves_next = algo.potential_moves(nextPiece, board)

	if holdPiece:
		potential_moves_hold = algo.potential_moves(holdPiece, board)

	bestPotential, maxScore, changed = check_moves(0, -9999999, potential_moves_next, board)
	bestPotential, maxScore, changed = check_moves(bestPotential, maxScore, potential_moves_hold, board)

	if DEBUG:
		print('\nPotential future moves from previous position: \n ')
		for coords in potential_moves_next:
			debug.print_coords(coords, board)
		for coords in potential_moves_hold:
			debug.print_coords(coords, board)
		print('Best score coords: With score of' + str(maxScore) + '\n')
		if changed:
			debug.print_coords(potential_moves_hold[bestPotential], board)
		else:
			debug.print_coords(potential_moves_next[bestPotential], board)

	if changed:
		return potential_moves_hold[bestPotential], maxScore, changed
	else:
		return potential_moves_next[bestPotential], maxScore, changed

if __name__ == "__main__":
	## Make sure to initiate with the jstris game windown in the primary screen with 100% zoom in
	## the game board, new game button, and the upcoming pieces must be full-sized (don't actually think that it resizes) and fully visible
	initiate()
	do_moves([])
	gameImg, forsightImg, holdImg = capture_inputs()
	gameState = gs.GameState(gameImg, forsightImg, holdImg)

	if DEBUG:
		gameState.debug_pretty_print()
		print(ev.evaluate(gameState.matrix))
		print('\n')

	coords, maxScore, changed = find_best_move(gameState.hold, gameState.next, gameState.matrix)

	capture_game('after.png')
	pyautogui.press('space', presses=10)
