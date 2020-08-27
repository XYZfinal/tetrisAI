import pyautogui
import time

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
	## capture command
	#pyautogui.screenshot('test.png', region=(LEFT, TOP, WIDTH, HEIGHT))

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

	pyautogui.screenshot('test.png', region=(LEFT, TOP, WIDTH, HEIGHT))

	### dummy ai to test usability of pyautogui (TO REMOVE)
	for i in range(10):
		pyautogui.press('left', presses=5)
		pyautogui.press('space')

	for i in range(10):
		pyautogui.press('right', presses=5)
		pyautogui.press('space')

	for i in range(10):
		pyautogui.press('space')

if __name__ == "__main__":
	## Make sure to initiate with the jstris game windown in the primary screen
	## the game board, new game button, and the upcoming pieces must be full-sized (don't actually think that it resizes) and fully visible
	initiate()