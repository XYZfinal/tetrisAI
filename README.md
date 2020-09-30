# tetrisAI

## Introduction

Tetris Algorithm implementation(with jstris as the simulator)

python version used: 3.8.3

Special credits to Yiyuan Lee on his post on tetris game evaluation https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/

## Libraries used and prerequisites

- pyautogui (for mouse, keyboard, and screenshotting capabilities)
- opencv (used in conjunction with pyautogui to help with screenshot processing)

pip install pyautogui

pip install opencv-python


## Development log

2020-08-27： Implemented jstris interactions (screenshotting the game board, starting the game, and implemented a dummy AI to test all functionalities)

2020-08-28: Discovered through testing the pixel RGB data for empty cells, block cells, and block shadow cells. Implemented an image processing construction of a matrix model of the game

2020-09-05: Added hold and forsight blocks recognition 

2020-09-09: Read article from Yiyuan Lee who used genetic algorithm to find optimal parameters for game state evaluator, will use the algorithm explained in the article for the first prototype.

	Several observations:
		- Bumpiness and line cleared are used as heuristics. This is fine when the game's aim is to clear as many lines as possible. Configurations will be necessary in the scenarios where we are aiming for a tetris (4 lines clear)
		- Considering that we will allow soft dropping and potentially t-spins down the roads, holes's parameters is expected to be not as harsh of an punishment



2020-09-10: Wrote game state evaluator in evaluate.py

2020-09-13: Wrote potential placement of next block in maximax.py

2020-09-14: Added selection of best potential moves based on evaluator

2020-09-20: Added function that gets the moves for a block to be placed into designated coordinates in maximax.py

2020-09-30：Debugged previous code and assembled everything into a first working prototype (included video for demonstration)
