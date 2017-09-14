

class Block:

	def __init__(self):
		self._color = [0xFF, 0xFF, 0xFF]
		self._dirty = True

	def setColor(self, value):
		self._dirty = True
		self._color = value

	def getColor(self):
		return self._color

	color = property(getColor, setColor)

	def getDirty(self):
		return self._dirty

	def clean(self):
		_dirty = False

	dirty = property(getDirty)
	
