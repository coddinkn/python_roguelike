import random

def generate(width, height, grid):
	random.seed()
	numberOfRooms = int(random.random() * 4) + 2
	for i in range(numberOfRooms):
		x = int(random.random() * width)
		y = int(random.random() * height)
		w = int(random.random() * ((width / 4) - 2)) + 3
		h = int(random.random() * ((5 * height) / 6)) + 3
		for j in range(int(w / 2)):
			if(x + j < width):
				grid[x + j][y] = '.'
			if(x - j >= 0):
				grid[x - j][y] = '.'
		for j in range(int(h / 2)):
			if(y + j < height):
				grid[x][y + j] = '.'
			if(y - j >= 0):
				grid[x][y - j] = '.'

class Level:
	
	def __init__(self, width, height, screen):
		self.width = width
		self.height = height
		self.screen = screen
		self.grid = [ [ ' ' for i in range(height) ] for j in range(width) ]
		generate(width, height, self.grid)

	def render(self):
		self.screen.clear()
		for x in range(self.width):
			for y in range(self.height):
				self.screen.addch(y, x, self.grid[x][y])

		
