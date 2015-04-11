from level import Level
from player import Player

class Dungeon:
	
	def __init__(self, width, height, depth, screen):
		self.currentDepth = 0;
		self.depth = depth
		self.levels = [ Level(width, height, screen) for i in range(depth) ]
		self.player = Player(self.levels[self.currentDepth].upX, self.levels[self.currentDepth].upY)
		self.levels[self.currentDepth].addEntity(self.player)
		
	def render(self):
		self.levels[self.currentDepth].render()
	
	def ascend(self):
		if(self.currentDepth > 0):
			self.currentDepth = self.currentDepth - 1

	def movePlayer(self, x, y):
		self.player.move(x, y)
			
	def descend(self):
		if(self.currentDepth < (self.depth - 1)): 
			self.currentDepth = self.currentDepth + 1		
