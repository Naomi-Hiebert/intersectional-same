

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
				self._blocks[x][y].setRandom()

	def __getitem__(self, key):
		return self._blocks[(key / self._height)][(key % self._height)]

	def get2d(self, x, y):
		return self._blocks[x][y]

	def getListIndex(self, x, y):
		return (x * self._height) + y

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

	def getAdjacent(self, index):
		adj = []
		x = self.getX(index)
		y = self.getY(index)
		if (x-1) >= 0:
			adj.append(self.getListIndex(x-1,y))
		if (x+1) < self._width:
			adj.append(self.getListIndex(x+1,y))
		if (y-1) >= 0:
			adj.append(self.getListIndex(x,y-1))
		if (y+1) < self._height:
			adj.append(self.getListIndex(x,y+1))
		return adj

	def remove(self, value):
		self.__getitem__(value).hide()

	def remove2d(self, x, y):
		self._blocks[x][y].hide()

	def compress(self):

		hiddenColumns = []
		for x in reversed(range(self._width)):

			#Reverse iterate over a column, removing all hidden blocks
			hiddenBlocks = []
			allHidden = True
			for y in reversed(range(self._height)):
				self._blocks[x][y].touch()
				if not self._blocks[x][y].visible:
					hiddenBlocks.append(self._blocks[x].pop(y))
				else:
					allHidden = False

			#and replace those hidden blocks at the top of the column
			self._blocks[x].extend(hiddenBlocks)

			#if everything was hidden, then the column was empty
			if allHidden:
				hiddenColumns.append(self._blocks.pop(x))

		self._blocks.extend(hiddenColumns)
		

	def findGroup(self, x, y):
		indices = []
		indices.append(self.getListIndex(x,y))
		
		for i in indices:
			for adj in self.getAdjacent(i):
				if self[i].isMatch(self[adj]) and adj not in indices:
					indices.append(adj)

		return indices


	def deleteGroup(self, indices):
		for i in indices:
			self.remove(i)

		self.compress()



	width = property(getWidth)
	height = property(getHeight)
	count = property(getCount)
