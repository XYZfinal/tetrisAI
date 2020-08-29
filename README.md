# tetrisAI
Minimax Algorithm implementation on tetris (with jstris as the simulator)

python version used: 3.8.3

======================================

Library dependencies:
- pyautogui (for mouse, keyboard, and screenshotting capabilities)
- opencv (used in conjunction with pyautogui to help with screenshot processing)

pip install pyautogui

pip install opencv-python


=====================================

Development log:

2020-08-27： Implemented jstris interactions (screenshotting the game board, starting the game, and implemented a dummy AI to test all functionalities)

2020-089-28 : Discovered through testing the pixel RGB data for empty cells, block cells, and block shadow cells. Implemented an image processing construction of a matrix model of the game
