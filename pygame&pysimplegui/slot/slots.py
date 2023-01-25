import pygame as pg
import sys
import numpy as np
import random as rand
pg.init()

width = 800
height = 800
lineWidth = 15
winLineWidth = 15
boardRows = 4
boardCols = 4
squareSize = 200
space = 55
windowName = "Slots"
windowNameInt = 0
cost = 1
#costtxt = "Cost: 1"
instructions = "Spin with left click, reset with R"
fontClr = (208,24,24)
player = 1
game_over = False

#Button settings
#1 means top point, 2 means bottom, 3 means either most left or right point
tri1L = (750, 730)
tri2L = (750, 790)
tri3L = (720, 760)
tri1R = (760, 730)
tri2R = (760, 790)
tri3R = (790, 760)

bgColor = (200, 200, 0)
lineColor = (0, 0, 180)
triangleColor = (255, 0, 0)
winLineColor = (220, 220, 220)

myFont = pg.font.SysFont(None, 50)
instrTxt = myFont.render(instructions, True, (fontClr))

screen = pg.display.set_mode((width, height))
pg.display.set_caption(windowName)
screen.fill(bgColor)
board = np.zeros((boardRows, boardCols))

def drawLines() :


	#Line 1 vert
	pg.draw.line(screen, lineColor, (0, squareSize), (width, squareSize), lineWidth)
	#Line 2 vert
	pg.draw.line(screen, lineColor, (0, 2 * squareSize), (width, 2 * squareSize), lineWidth)
	#Line 3 vert
	pg.draw.line(screen, lineColor, (0, 3 * squareSize), (width, 3 * squareSize), lineWidth)
	#Line 1 hori
	pg.draw.line(screen, lineColor, (squareSize, 0), (squareSize, height), lineWidth)
	#Line 2 hori
	pg.draw.line(screen, lineColor, (2 * squareSize, 0), (2 * squareSize, height), lineWidth)
	#Line 3 hori
	pg.draw.line(screen, lineColor, (3 * squareSize, 0), (3 * squareSize, height), lineWidth)

	#Instructions
	screen.blit(instrTxt, (5, 5))

""" 
def drawPointSyst() :

	#(rightest point)(top point)(bottom point)
	pg.draw.polygon(screen, (triangleColor), ((tri3R), (tri1R), (tri2R)))
	#(leftest point)(top point)(bottom point)
	pg.draw.polygon(screen, (triangleColor), ((tri3L), (tri1L), (tri2L)))


	myFont = pg.font.SysFont(None, 50)
	textSurface = myFont.render(costtxt, True, (fontClr))
	#(x,y)
	screen.blit(textSurface, (560, 750))

 """

snake1 = pg.image.load("snake.png")
snake2 = pg.image.load("blackSnake.png")

def drawShapes() :
	for row in range(boardRows) :
		for col in range(boardCols) :
			if board[row][col] == 1 :
				screen.blit(snake2, (int( col * squareSize + squareSize//2 - 32), int( row * squareSize + squareSize//2 - 32)))
			elif board[row][col] == 2 :
				screen.blit(snake1, (int( col * squareSize + squareSize//2 - 32), int( row * squareSize + squareSize//2 - 32)))

def markSquare(row, col) :
	shape = rand.randint(1,2)
	board[row][col] = shape

def freeSquare(row, col):
	return board[row][col] == 0

def boardCheck():
	for row in range(boardRows) :
		for col in range(boardCols) :
			if board[row][col] == 0 :
				return False

	return True

def checkWin(player, cost) :
	global windowNameInt

	#All vertical
	for col in range(boardCols) :
		if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][col] == player :
			vertWinLine(col)
			windowNameInt += 1
			cost += 1

	#All horizontal
	for row in range(boardRows) :
		if board[row][0] == player and board[row][1] == player and board[row][2] == player and board[row][3] == player :
			horiWinLine(row)
			windowNameInt += 1

	#From bottom right to top left
	if board[3][0] == player and board[2][1] == player and board[1][2] == player and board[0][3] == player :
		drawAscDiagonal()
		windowNameInt += 1

	#From top left to bottom right
	if board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player :
		drawDescDiagonal()
		windowNameInt += 1

def vertWinLine(col) :
	posX = col * squareSize + squareSize//2
	
	color = winLineColor
	pg.draw.line(screen, color, (posX, 15), (posX, height - 15), lineWidth)
	print("verti win")

def horiWinLine(row) :
	posY = row * squareSize + squareSize//2

	color = winLineColor
	pg.draw.line(screen, color, (15, posY), (width - 15, posY), winLineWidth)
	print("hori win")

def drawAscDiagonal() :

	color = winLineColor
	pg.draw.line(screen, color, (15, height - 15), (width - 15, 15), winLineWidth)
	print("asc win")

def drawDescDiagonal() :

	color = winLineColor
	pg.draw.line(screen, color, (15, 15), (width - 15, height - 15), winLineWidth)
	print("diag win")

def restart() :
	screen.fill(bgColor)
	drawLines()
	# drawPointSyst()
	windowName = (str(windowNameInt))
	pg.display.set_caption(windowName)
	for row in range(boardRows) :
		for col in range(boardCols) :
			board[row][col] = 0

drawLines()
# drawPointSyst()

def posCheckLeft(pos) :
	x, y = pos
	return 720 < x < 750 and 730 < y < 790

def posCheckRight(pos) :
	x, y = pos
	return 760 < x < 790 and 730 < y < 790


def game(cost) :
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.MOUSEBUTTONDOWN:
			pos = pg.mouse.get_pos()
			print(pos)
			if posCheckLeft(pos) :
				print("left")
				cost += 1			
				costtxt = "Cost: {}".format(cost)
				myFont = pg.font.SysFont(None, 50)
				textSurface = myFont.render(costtxt, True, (fontClr))
				screen.blit(textSurface, (560, 750))

			elif posCheckRight(pos) :
				print("right")
				cost += 1		
				costtxt = "Cost: {}".format(cost)
				myFont = pg.font.SysFont(None, 50)
				textSurface = myFont.render(costtxt, True, (fontClr))
				screen.blit(textSurface, (560, 750))

			else :
				while not boardCheck() :
					randMouseX = rand.randint(0, width - 1)
					randMouseY = rand.randint(0, height - 1)

					clickedRow = int(randMouseY // squareSize)
					clickedCol = int(randMouseX // squareSize)
					# print("Click ", pos, "Grid coordinates: ", clickedRow, clickedCol)
					
					if freeSquare(clickedRow, clickedCol) :

						markSquare(clickedRow, clickedCol)
						drawShapes()
				checkWin(1, cost)
				checkWin(2, cost)
			
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_r:
				restart()
				
	pg.display.update()

while True: game(cost)
