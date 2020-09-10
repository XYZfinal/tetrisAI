
### Creds to Yiyuan Lee for providing optimal parameters for evaluation calculation

AGGREGATE_HEIGHT_PARAMETER = -0.510066
COMPLETED_LINES_PARAMETER = 0.760666
HOLES_PARAMETER = -0.35663
BUMPINESS_PARAMETER = -0.184483

def evaluate(matrix):
	columnHeight = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	holes = 0
	completedLines = 0
	aggregateHeight = 0
	bumpiness = 0
	## Parse through the matrix scouting for info
	for row in range(20):
		completed = True
		for column in range(10):
			if matrix[row][column] != 'E':
				if row > columnHeight[column]:
					columnHeight[column] = row
			else:
				completed = False
				if columnHeight[column] > row:
					holes += 1
		if completed:
			completedLines += 1

	for i in range(10):
		aggregateHeight += columnHeight[i]
		if i > 0:
			bumpiness += abs(columnHeight[i-1] - columnHeight[i])

	resultScore = AGGREGATE_HEIGHT_PARAMETER * aggregateHeight
	resultScore += COMPLETED_LINES_PARAMETER * completedLines
	resultScore += HOLES_PARAMETER * holes
	resultScore += BUMPINESS_PARAMETER * bumpiness
	return resultScore
