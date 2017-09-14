

class Block:

	def __init__(self):
		self._color1 = [0xFF, 0xFF, 0xFF]
		self._color2 = [0x88, 0x88, 0x88]
		self._dirty = True
		self._visible = True

	def setColor1(self, value):
		self._dirty = True
		self._color1 = value

	def getColor1(self):
		return self._color1

	def setColor2(self, value):
		self._dirty = True
		self._color2 = value

	def getColor2(self):
		return self._color2

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
	color2 = property(getColor2, setColor2)
	dirty = property(getDirty)
	visible = property(getVisible)
	
