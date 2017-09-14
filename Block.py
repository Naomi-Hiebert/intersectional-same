

class Block:

	def __init__(self):
		self._color1 = [0xFF, 0xFF, 0xFF]
		self._dirty = True
		self._visible = True

	def setColor1(self, value):
		self._dirty = True
		self._color1 = value

	def getColor1(self):
		return self._color1

	def getDirty(self):
		return self._dirty

	def clean(self):
		_dirty = False

	def getVisible(self):
		return self._visible

	def hide(self):
		_visible = False

	def show(self):
		_visible = True

	color1 = property(getColor1, setColor1)
	dirty = property(getDirty)
	visible = property(getVisible)
	
