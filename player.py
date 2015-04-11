import random

class Player:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.c = '@'
		self.oldX = x
		self.oldY = y
		self.aiMovable = False
		self.health = 10

	def move(self, x, y):
		self.oldX = self.x
		self.oldY = self.y
		self.x += x
		self.y += y

	def attack(self, entity):
		random.seed()
		if random.random() > 0.5:
			entity.health -= 1
