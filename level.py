class Level:
	
	def __init__(self, width, height, screen):
		self.width = width
		self.height = height
		self.screen = screen
		self.grid = [ [ 'g' for i in range(width) ] for j in range(height) ]
	
	def render(self):
		self.screen.clear()
		for x in range(self.width):
			for y in range(self.height):
				self.screen.addch(y, x)

		
