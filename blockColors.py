## Empty black pixel
EMPTY = (0, 0, 0)

## All RGB pixels for each block
S_BLOCK = (89, 177, 1)
Z_BLOCK = (215, 15, 55)
L_BLOCK = (227, 91, 2)
J_BLOCK = (33, 65, 198)
O_BLOCK = (227, 159, 2)
I_BLOCK = (15, 155, 215)
T_BLOCK = (175, 41, 138)

## All RGB pixels for each block shadow
S_BLOCK_SHADOW = (44, 88, 0)
Z_BLOCK_SHADOW = (107, 7, 27)
L_BLOCK_SHADOW = (113, 45, 1)
J_BLOCK_SHADOW = (16, 32, 99)
O_BLOCK_SHADOW = (113, 79, 1)
I_BLOCK_SHADOW = (7, 77, 107)
T_BLOCK_SHADOW = (87, 20, 69)

def initiate_colors(calibrationUsed):
	global S_BLOCK
	global Z_BLOCK
	global L_BLOCK
	global J_BLOCK
	global O_BLOCK
	global I_BLOCK
	global T_BLOCK
	
	if calibrationUsed == 'leftUpCorner.JPG':
		S_BLOCK = (89, 177, 1)
		Z_BLOCK = (215, 15, 55)
		L_BLOCK = (227, 91, 2)
		J_BLOCK = (33, 65, 198)
		O_BLOCK = (227, 159, 2)
		I_BLOCK = (15, 155, 215)
		T_BLOCK = (175, 41, 138)
	elif calibrationUsed == 'MACleftUpCorner.JPG':
		S_BLOCK = (92, 175, 31)
		Z_BLOCK = (213, 22, 59)
		L_BLOCK = (225, 91, 29)
		J_BLOCK = (36, 70, 195)
		O_BLOCK = (225, 158, 37)
		I_BLOCK = (32, 156, 213)
		T_BLOCK = (173, 46, 137)
	else:
		S_BLOCK = (89, 177, 1)
		Z_BLOCK = (215, 15, 55)
		L_BLOCK = (227, 91, 2)
		J_BLOCK = (33, 65, 198)
		O_BLOCK = (227, 159, 2)
		I_BLOCK = (15, 155, 215)
		T_BLOCK = (175, 41, 138)