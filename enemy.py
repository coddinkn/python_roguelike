import random

class Enemy:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.oldX = x
		self.oldY = y
		self.aiMovable = True
		self.c = 'e'

	def move(self):
		self.oldX = self.x
		self.oldY = self.y
		random.seed()
		if(random.random() > 0.25):	
			if(random.random() > 0.5):
				self.x += 1
			else:
				self.x -= 1	
		if(random.random() > 0.25):	
			if(random.random() > 0.5):
				self.y += 1
			else:
				self.y -= 1	
