class Player:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.c = '@'

	def move(self, x, y):
		self.x += x
		self.y += y
