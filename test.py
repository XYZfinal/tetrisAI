import pyautogui

## test program of drawing a square spiral in paint with cursor on paint
def square_spiral():
	distance = 200
	while distance > 0:
		pyautogui.drag(distance, 0, duration=0.5)   # move right
		distance -= 5
		pyautogui.drag(0, distance, duration=0.5)   # move down
		pyautogui.drag(-distance, 0, duration=0.5)  # move left
		distance -= 5
		pyautogui.drag(0, -distance, duration=0.5)  # move up

## test progrm to enter text into microsoft word
pyautogui.click()
pyautogui.write('Hello world!', interval=0.01)
for i in range(200):
	pyautogui.press('space', presses = 5)