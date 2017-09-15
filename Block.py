import random

class Block:

	colorTable1 = 	[[0xFF, 0xFF, 0x00],
					 [0x88, 0x88, 0x00],
					 [0x00, 0x00, 0xCC],
					 [0x66, 0x66, 0xFF]]

	colorTable2 = 	[[0xFF, 0xFF, 0xFF],
					 [0xBB, 0xBB, 0xBB],
					 [0x88, 0x88, 0x88],
					 [0x44, 0x44, 0x44]]

	def __init__(self):
		self._active = 1
		self._color1 = 0
		self._color2 = 0
		self._dirty = True
		self._visible = True


	def setColor1(self, value):
		self._color1 = value
		if self._visible:
			self._dirty = True

	def showColor1(self):
		if self._visible:
			return self.colorTable1[self._color1] + self.getAlpha()
		else:
			return [0x00, 0x00, 0x00, 0x00]

	def getColor1(self):
		return self._color1

	def setColor2(self, value):
		self._color2 = value
		if self._visible:
			self._dirty = True

	def showColor2(self):
		if self._visible:
			return self.colorTable2[self._color2] + self.getAlpha()
		else:
			return [0x00, 0x00, 0x00, 0x00]
	def getColor2(self):
		return self._color2

	def getDirty(self):
		return self._dirty

	def getAlpha(self):
		if self._visible:
			return [0xFF]
		else:
			return [0x00]

	def clean(self):
		self._dirty = False

	def touch(self):
		self._dirty = True

	def getVisible(self):
		return self._visible

	def hide(self):
		self._visible = False
		self._dirty = True

	def show(self):
		self._visible = True
		self._dirty = True

	def getActive(self):
		return self._active

	def setActive(self, value):
		self._active = value
		if self._visible:
			self._dirty = True

	def showActive1(self):
		if self._active == 2:
			return self.showColor2()
		else:
			return self.showColor1()

	def showActive2(self):
		if self._active == 1:
			return self.showColor1()
		else:
			return self.showColor2()

	def setRandom(self):
		r = random.randint(0, 15)
		self._color1 = r / 4
		self._color2 = r % 4
		self._dirty = True

	def isMatch(self, other):
		if self._visible and other.visible:
			if self._active == 1 and self.color1 == other.color1:
				return True
			if self._active == 2 and self.color2 == other.color2:
				return True
		return False

	color1 = property(getColor1, setColor1)
	color2 = property(getColor2, setColor2)
	alpha = property(getAlpha)
	dirty = property(getDirty)
	visible = property(getVisible)
	active = property(getActive, setActive)
	
