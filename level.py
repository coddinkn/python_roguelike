import random
from enemy import Enemy

def generate(width, height, grid):
	random.seed()
	numberOfRooms = int(random.random() * 4) + 2
	lastX = 0
	for i in range(numberOfRooms):
		y = int((height / 3) + (random.random() * (height * (1/3))))
		while True:
			x = int((width / 6) + (random.random() * ((3/5) * width)))
			if ((lastX == 0) or (abs(lastX - x) < (width / 6))):
				break
			lastX = x
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
		for j in range(w):
			for k in range(h):
				if (((x - (w / 2) + j) < width) and ((y - (h / 2) + k) < height) and not (((w / 2) + j) > (w + 1)) and not (((h / 2) + k) > (h + 1))):
					grid[int(x - (w / 2) + j)][int(y - (h / 2) + k)] = '.' 
	skip = 2
	for i in range(height):
		makeHall = False
		startX = 0
		endX = 0
		if skip == 0:
			for j in range(width):
				if (grid[j][i] == '.' and grid[j+1][i] == ' '):
					makeHall = True
					startX = j + 1
					continue
				if (makeHall and grid[j][i] == '.'):
					endX = j-1
					break
			for j in range(startX, endX + 1):
				if makeHall:
					grid[j][i] = '#'
			if makeHall:
				skip += 3
		else:
			skip -= 1
	skip = 2
	for i in range(width):
		makeHall = False
		startY = 0
		endY = 0
		if skip == 0:
			for j in range(height):
				if (grid[i][j] == '.' and (j + 1 < height) and grid[i][j+1] == ' '):
					makeHall = True
					startY = j + 1
					continue
				if (makeHall and grid[i][j] == '.'):
					endY = j-1
					break
			for j in range(startY, endY + 1):
				if makeHall:
					grid[i][j] = '#'
			if makeHall:
				skip += 3
		else:
			skip -= 1

def addStuff(width, height, grid):
	random.seed()
	downXpos = random.random() * width
	upXpos = random.random() * width
	downYpos = random.random() * height
	upYpos = random.random() * height
	while (grid[int(upXpos)][int(upYpos)] != '.'):
		upXpos = random.random() * width
		upYpos = random.random() * height
	grid[int(upXpos)][int(upYpos)] = '>'
	while (grid[int(downXpos)][int(downYpos)] != '.'):
		downXpos = random.random() * width
		downYpos = random.random() * height
	grid[int(downXpos)][int(downYpos)] = '<'
	return (int(upXpos), int(upYpos), int(downXpos), int(downYpos))


class Level:
	
	def __init__(self, width, height, screen):
		self.width = width
		self.height = height
		self.screen = screen	
		self.grid = [ [ ' ' for i in range(height) ] for j in range(width) ]
		self.entityGrid = [ [ ' ' for i in range(height) ] for j in range(width) ]
		self.itemGrid = [ [ ' ' for i in range(height) ] for j in range(width) ]
		generate(width, height, self.grid)
		stairPos = addStuff(width, height, self.grid)
		self.upX = stairPos[0]
		self.upY = stairPos[1]
		self.downX = stairPos[2]
		self.downY = stairPos[3]
		self.entityList = []
		random.seed()	
		numberOfEnemies = int(random.random() * 10)
		for i in range(numberOfEnemies):
			self.addEntity(Enemy(int(random.random() * width), int(random.random() * height)))

	def addEntity(self, entity):
		x = entity.x
		y = entity.y
		if((x >= 0 and x < self.width) and (y >= 0 and y < self.height)):
			if(self.grid[x][y] != ' '):
				self.entityList.append(entity)
				self.entityGrid[x][y] = entity.c

	def removeEntityAt(self, x, y):
		for entity in self.entityList:
			if(entity.x == x and entity.y == y):
				self.entityList.remove(entity)

	def update(self):
		for x in range(self.width):
			for y in range(self.height):
				self.entityGrid[x][y] = ' '
		for entity in self.entityList:
			x = entity.x
			y = entity.y
			if entity.aiMovable:
				entity.move()
			if((x >= 0 and x < self.width) and (y >= 0 and y < self.height)):
				if(self.grid[x][y] != ' '):
					self.entityGrid[x][y] = entity.c
				else:
					entity.x = entity.oldX
					entity.y = entity.oldY
					if entity.aiMovable == False:	
						self.entityGrid[entity.x][entity.y] = entity.c
						self.screen.addstr(self.height + 1, 0, "you cant go that way silly")
			else:
				entity.x = entity.oldX
				entity.y = entity.oldY
				if entity.aiMovable == False:
					self.entityGrid[entity.x][entity.y] = entity.c
					self.screen.addstr(self.height + 1, 0, "you cant go that way silly")
	
	def render(self):
		self.update()
		for x in range(self.width):
			for y in range(self.height):
				self.screen.addch(y, x, self.grid[x][y])
				if(self.entityGrid[x][y] != ' '):
					self.screen.addch(y, x, self.entityGrid[x][y])
