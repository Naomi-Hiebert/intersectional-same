import pyglet
import Block
import BlockArray
import random



#magic numbers
blockSize = 24
pointSize = 6
halfBorder = 1.0
height = 24
width = 36

#ugly global variables for visual effects
hoverGroup = []

#initialize the most important data structure
blocks = BlockArray.BlockArray(width, height)

#initialize the graphics
window = pyglet.window.Window(width*blockSize, height*blockSize)
pyglet.gl.glPointSize(pointSize)

triField = pyglet.graphics.vertex_list(blocks.count * 6, 'v2f', 'c4B')
triField.vertices = [0.0] * (blocks.count * 12)
triField.colors = [0xFF] * (blocks.count * 24)

pointField1 = pyglet.graphics.vertex_list(blocks.count, 'v2f', 'c4B')
pointField1.vertices = [0.0] * (blocks.count * 2)
pointField1.colors = [0xFF] * (blocks.count * 4)

pointField2 = pyglet.graphics.vertex_list(blocks.count, 'v2f', 'c4B')
pointField2.vertices = [0.0] * (blocks.count * 2)
pointField2.colors = [0xFF] * (blocks.count * 4)


for i in range(blocks.count):
	x = blocks.getX(i) * float(blockSize)
	y = blocks.getY(i) * float(blockSize)

	triField.vertices[(i*12)+0] = x + halfBorder
	triField.vertices[(i*12)+1] = y + halfBorder

	triField.vertices[(i*12)+2] = x + float(blockSize) - halfBorder
	triField.vertices[(i*12)+3] = y + float(blockSize) - halfBorder

	triField.vertices[(i*12)+4] = x + float(blockSize) - halfBorder
	triField.vertices[(i*12)+5] = y + halfBorder

	triField.vertices[(i*12)+6] = x + halfBorder
	triField.vertices[(i*12)+7] = y + halfBorder

	triField.vertices[(i*12)+8] = x + float(blockSize) - halfBorder
	triField.vertices[(i*12)+9] = y + float(blockSize) - halfBorder

	triField.vertices[(i*12)+10] = x + halfBorder
	triField.vertices[(i*12)+11] = y + float(blockSize) - halfBorder

	pointField1.vertices[(i*2)] = x + (pointSize/2.0) + halfBorder
	pointField1.vertices[(i*2)+1] = y + float(blockSize) - (pointSize / 2.0) - halfBorder

	pointField2.vertices[(i*2)] = x + float(blockSize) - (pointSize / 2.0) - halfBorder
	pointField2.vertices[(i*2)+1] = y + (pointSize/2.0) + halfBorder

def unHighlight():
	global hoverGroup
	global halfBorder

	for i in hoverGroup:
		triField.vertices[(i*12)+0] += halfBorder
		triField.vertices[(i*12)+1] += halfBorder

		triField.vertices[(i*12)+2] -= halfBorder
		triField.vertices[(i*12)+3] -= halfBorder

		triField.vertices[(i*12)+4] -= halfBorder
		triField.vertices[(i*12)+5] += halfBorder

		triField.vertices[(i*12)+6] += halfBorder
		triField.vertices[(i*12)+7] += halfBorder

		triField.vertices[(i*12)+8] -= halfBorder
		triField.vertices[(i*12)+9] -= halfBorder

		triField.vertices[(i*12)+10] += halfBorder
		triField.vertices[(i*12)+11] -= halfBorder

	hoverGroup = []

def highlightHover(toHighlight):
	global hoverGroup
	global halfBorder
	
	unHighlight()
	hoverGroup = toHighlight[:]

	for i in hoverGroup:
		triField.vertices[(i*12)+0] -= halfBorder
		triField.vertices[(i*12)+1] -= halfBorder

		triField.vertices[(i*12)+2] += halfBorder
		triField.vertices[(i*12)+3] += halfBorder

		triField.vertices[(i*12)+4] += halfBorder
		triField.vertices[(i*12)+5] -= halfBorder

		triField.vertices[(i*12)+6] -= halfBorder
		triField.vertices[(i*12)+7] -= halfBorder

		triField.vertices[(i*12)+8] += halfBorder
		triField.vertices[(i*12)+9] += halfBorder

		triField.vertices[(i*12)+10] -= halfBorder
		triField.vertices[(i*12)+11] += halfBorder


@window.event
def on_draw():

	for b in range(blocks.count):
		if blocks[b].dirty:
			pointField1.colors[b * 4:(b+1) * 4] = blocks[b].showColor1()
			pointField2.colors[b * 4:(b+1) * 4] = blocks[b].showColor2()
			triField.colors[b * 24:(b * 24) + 12] = blocks[b].showActive2() * 3
			triField.colors[(b * 24) + 12:(b * 24) + 24] = blocks[b].showActive1() * 3
			blocks[b].clean()
				
	window.clear()
	triField.draw(pyglet.gl.GL_TRIANGLES)
	pointField1.draw(pyglet.gl.GL_POINTS)
	pointField2.draw(pyglet.gl.GL_POINTS)

@window.event
def on_mouse_press(x, y, button, modifiers):

	indexX = x/blockSize
	indexY = y/blockSize
	if indexX < blocks.width and indexY < blocks.height and x >= 0 and y >= 0:
		delGroup = blocks.findGroup(indexX,indexY)

		if delGroup.count >= 3:
			unHighlight()
			blocks.deleteGroup(delGroup)
		
@window.event
def on_key_press(symbol, modifiers):
	
	if symbol == pyglet.window.key.SPACE:
		for b in range(blocks.count):
			blocks[b].setActive(2)
		unHighlight()

@window.event
def on_key_release(symbol, modifiers):
	
	if symbol == pyglet.window.key.SPACE:
		for b in range(blocks.count):
			blocks[b].setActive(1)
		unHighlight()

@window.event
def on_mouse_motion(x, y, dx, dy):

	global hoverGroup

	indexX = x/blockSize
	indexY = y/blockSize
	if indexX < blocks.width and indexY < blocks.height and x >= 0 and y >= 0:
		if blocks.getListIndex(indexX, indexY) not in hoverGroup:
			if len(blocks.findGroup(indexX, indexY)) >= 3:
				highlightHover(blocks.findGroup(indexX, indexY))
			else:
				unHighlight()
	else:
		unHighlight()

@window.event
def on_mouse_leave(x,y):
	unHighlight()


	


pyglet.app.run()

