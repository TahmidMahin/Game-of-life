import pygame as pg
import math

pg.init()
black = (0, 0, 0)
yellow = (255, 255, 0)
grey = (127, 127, 127)

width = 1200
height = 600

screen = pg.display.set_mode((width, height))
pg.display.set_caption("game of life")

grid = []
length = 10

class grid_cell:

	def __init__(self, x, y, cell_length):
		self.x = x
		self.y = y
		self.cell_length = cell_length
		self.cell_color = black

	def toggle_state(self):
		if self.cell_color == black:
			self.cell_color = yellow
		else:
			self.cell_color = black

	def show_cell(self):
		pg.draw.rect(screen, self.cell_color, (self.x,self.y,self.cell_length,self.cell_length))

def make_grid():
	for y in range(0, height, length):
		row = []
		for x in range(0, width, length):
			row.append(grid_cell(x+1,y+1,length-2))
		grid.append(row)

def show_grid():
	for row in grid:
		for cell in row:
			cell.show_cell()

def count_neighbour(i, j):
	count = 0
	if i != len(grid)-1:
		count += 1 if grid[i+1][j].cell_color == yellow else 0
	if i != len(grid)-1 and j != len(grid[i])-1:
		count += 1 if grid[i+1][j+1].cell_color == yellow else 0
	if j != len(grid[i])-1:
		count += 1 if grid[i][j+1].cell_color == yellow else 0
	if i != 0 and j != len(grid[i])-1:
		count += 1 if grid[i-1][j+1].cell_color == yellow else 0
	if i != 0:
		count += 1 if grid[i-1][j].cell_color == yellow else 0
	if i != 0 and j != 0:
		count += 1 if grid[i-1][j-1].cell_color == yellow else 0
	if j != 0:
		count += 1 if grid[i][j-1].cell_color == yellow else 0
	if i != len(grid)-1 and j != 0:
		count += 1 if grid[i+1][j-1].cell_color == yellow else 0
	return count


def update_grid():
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			grid[i][j].cell_neighbour = count_neighbour(i, j)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j].cell_color == black and grid[i][j].cell_neighbour == 3:
				grid[i][j].toggle_state()
			elif grid[i][j].cell_color==yellow and (grid[i][j].cell_neighbour>3 or grid[i][j].cell_neighbour<2):
				grid[i][j].toggle_state()

def simulate():
	time_step = 0
	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					running = False

		screen.fill(grey)
		show_grid()
		time_step += 1
		if time_step == 10:
			time_step = 0
			update_grid()
		pg.display.update()

	return True

def initialize():
	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
			if event.type == pg.MOUSEBUTTONDOWN:
				x, y = pg.mouse.get_pos()
				grid[y//length][x//length].toggle_state()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					running = simulate()

		screen.fill(grey)
		show_grid()
		pg.display.update()

make_grid()
initialize()

