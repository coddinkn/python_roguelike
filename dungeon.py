from level import Level

class Dungeon:
	
	def __init__(self, width, height, depth, screen):
		self.currentDepth = 0;
		self.depth = depth
		self.levels = [ Level(width, height, screen) for i in range(depth) ]
	
	def render(self):
		self.levels[self.currentDepth].render()
	
	def ascend(self):
		if(self.currentDepth > 0):
			self.currentDepth = self.currentDepth - 1
			
	def descend(self):
		if(self.currentDepth < (self.depth - 1)): 
			self.currentDepth = self.currentDepth + 1		
