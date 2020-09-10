import pyautogui
import time
import GameState as gs
import evaluate as  ev

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

def initiate():
	## Suicide 1 game, making sure the left top corner is untouched for screenprint calibration
	initiate_game()
	pyautogui.press('space', 20)
	calibrate()
	initiate_game()

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

if __name__ == "__main__":
	## Make sure to initiate with the jstris game windown in the primary screen with 100% zoom in
	## the game board, new game button, and the upcoming pieces must be full-sized (don't actually think that it resizes) and fully visible
	initiate()
	do_moves([])
	gameImg, forsightImg, holdImg = capture_inputs()
	gameState = gs.GameState(gameImg, forsightImg, holdImg)
	gameState.debug_pretty_print()
	print(ev.evaluate(gameState.matrix))
	capture_game('after.png')
	pyautogui.press('space', presses=10)
