

import Block

class BlockArray:
	

	def __init__(self, width, height):
		self._width = width
		self._height = height
		self._blocks = [None] * width

		for x in range(width):
			self._blocks[x] = [None] * height
			for y in range(height):
				self._blocks[x][y] = Block.Block()

	def __getitem__(self, key):
		return self._blocks[(key / self._height)][(key % self._height)]

	def get2d(self, x, y):
		return self._blocks[x][y]

	def getListIndex(self, x, y):
		return (x*self._height) + y

	def getX(self, index):
		return index / self._height

	def getY(self, index):
		return index % self._height

	def getWidth(self):
		return self._width

	def getHeight(self):
		return self._height

	def getCount(self):
		return self._height * self._width

	width = property(getWidth)
	height = property(getHeight)
	count = property(getCount)
