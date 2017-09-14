import pyglet
import Block
import BlockArray
import random



#magic numbers
blockSize = 64
pointSize = 8
height = 8
width = 12

#initialize the most important data structure
blocks = BlockArray.BlockArray(width, height)

#initialize the graphics
window = pyglet.window.Window(width*blockSize, height*blockSize)
pyglet.gl.glPointSize(pointSize)

pointField1 = pyglet.graphics.vertex_list(blocks.count, 'v2f', 'c4B')
pointField1.vertices = [0.0] * (blocks.count * 2)
pointField1.colors = [0xFF] * (blocks.count * 4)

for i in range(blocks.count):
	pointField1.vertices[(i * 2)] = (blocks.getX(i) * 1.0 * blockSize) + (pointSize/2.0)
	pointField1.vertices[(i * 2) + 1] = (blocks.getY(i) * 1.0 * blockSize) + (pointSize/2.0)


pointField2 = pyglet.graphics.vertex_list(blocks.count, 'v2f', 'c4B')
pointField2.vertices = [0.0] * (blocks.count * 2)
pointField2.colors = [0xFF] * (blocks.count * 4)

for i in range(blocks.count):
	pointField2.vertices[(i * 2)] = ((blocks.getX(i) + 1.0) * blockSize) - (pointSize / 2.0)
	pointField2.vertices[(i * 2) + 1] = ((blocks.getY(i) + 1.0) * blockSize) - (pointSize / 2.0)

@window.event
def on_draw():

	for b in range(blocks.count):
		if blocks[b].dirty:
			pointField1.colors[b * 4:(b * 4) + 3] = blocks[b].color1
			pointField2.colors[b * 4:(b * 4) + 3] = blocks[b].color2
			blocks[b].clean()
				
	window.clear()
	pointField1.draw(pyglet.gl.GL_POINTS)
	pointField2.draw(pyglet.gl.GL_POINTS)

@window.event
def on_mouse_press(x, y, button, modifiers):

	indexX = x/blockSize
	indexY = y/blockSize
	if indexX < blocks.width and indexY < blocks.height and x > 0 and y > 0:
		listIndex = blocks.getListIndex(indexX, indexY)
		blocks[listIndex].color2 = blocks[listIndex].color1
		blocks[listIndex].color1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


pyglet.app.run()

