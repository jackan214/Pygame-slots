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
circleRadius = 50
circleWidth = 15
crossWidth = 25
space = 55
windowName = "Slots"
windowNameInt = 0

bgColor = (200, 200, 0)
lineColor = (0, 0, 180)
winLineColor = (220, 220, 220)
circleColor = (239, 231, 200)
crossColor = (66, 66, 66)

screen = pg.display.set_mode((width, height))
pg.display.set_caption(windowName)
screen.fill(bgColor)
board = np.zeros((boardRows, boardCols))

def drawLines():
	
	pg.draw.line(screen, lineColor, (0, squareSize), (width, squareSize), lineWidth)
	
	pg.draw.line(screen, lineColor, (0, 2 * squareSize), (width, 2 * squareSize), lineWidth)

	pg.draw.line(screen, lineColor, (0, 3 * squareSize), (width, 3 * squareSize), lineWidth)

	pg.draw.line(screen, lineColor, (squareSize, 0), (squareSize, height), lineWidth)

	pg.draw.line(screen, lineColor, (2 * squareSize, 0), (2 * squareSize, height), lineWidth)

	pg.draw.line(screen, lineColor, (3 * squareSize, 0), (3 * squareSize, height), lineWidth)

snake1 = pg.image.load("snake.png")
snake2 = pg.image.load("blackSnake.png")

def drawShapes():
	for row in range(boardRows):
		for col in range(boardCols):
			if board[row][col] == 1:
				screen.blit(snake2, (int( col * squareSize + squareSize//2 ), int( row * squareSize + squareSize//2 )))				
			elif board[row][col] == 2:
				screen.blit(snake1, (int( col * squareSize + squareSize//2 ), int( row * squareSize + squareSize//2 )))

def markSquare(row, col):
	shape = rand.randint(1,2)
	board[row][col] = shape

def freeSquare(row, col):
	return board[row][col] == 0

def boardCheck():
	for row in range(boardRows):
		for col in range(boardCols):
			if board[row][col] == 0:
				return False

	return True

def checkWin(player):
	global windowNameInt
	for col in range(boardCols):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][col] == player:
			vertWinLine(col)
			windowNameInt += 1

	for row in range(boardRows):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player and board[row][3] == player:
			horiWinLine(row)
			windowNameInt += 1

	if board[3][0] == player and board[2][1] == player and board[1][2] == player and board[0][3] == player:
		drawAscDiagonal()
		windowNameInt += 1

	if board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player:
		drawDescDiagonal()
		windowNameInt += 1


def vertWinLine(col):
	posX = col * squareSize + squareSize//2
	
	color = winLineColor
	pg.draw.line(screen, color, (posX, 15), (posX, height - 15), lineWidth)
	print("verti win")

def horiWinLine(row):
	posY = row * squareSize + squareSize//2

	color = winLineColor
	pg.draw.line(screen, color, (15, posY), (width - 15, posY), winLineWidth)
	print("hori win")

def drawAscDiagonal():

	color = winLineColor
	pg.draw.line(screen, color, (15, height - 15), (width - 15, 15), winLineWidth)
	print("asc win")

def drawDescDiagonal():

	color = winLineColor
	pg.draw.line(screen, color, (15, 15), (width - 15, height - 15), winLineWidth)
	print("diag win")

def restart():
	screen.fill(bgColor)
	drawLines()
	windowName = (str(windowNameInt))
	pg.display.set_caption(windowName)
	for row in range(boardRows):
		for col in range(boardCols):
			board[row][col] = 0

drawLines()

player = 1
game_over = False


def game() :
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.MOUSEBUTTONDOWN:
			pos = pg.mouse.get_pos()
			while not boardCheck() :
				
				randMouseX = rand.randint(0, width - 1)
				randMouseY = rand.randint(0, height - 1)

				clicked_row = int(randMouseY // squareSize)
				clicked_col = int(randMouseX // squareSize)
				print("Click ", pos, "Grid coordinates: ", clicked_row, clicked_col)
				
				if freeSquare(clicked_row, clicked_col):

					markSquare(clicked_row, clicked_col)
					drawShapes()
					
			checkWin(1)
			checkWin(2)

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_r:
				restart()
				
	pg.display.update()

while True: game()