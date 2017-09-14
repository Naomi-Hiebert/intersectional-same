import pyglet
import Block
import BlockArray
import random

window = pyglet.window.Window()

pyglet.gl.glPointSize(8.0)

blockSize = 64.0
blocks = BlockArray.BlockArray(10, 7)


blockField = pyglet.graphics.vertex_list(blocks.count, 'v2f', 'c4B')
blockField.vertices = [0.0] * (blocks.count * 2)
blockField.colors = [0xFF] * (blocks.count * 4)

for i in range(blocks.count):
	blockField.vertices[(i * 2)] = ((blocks.getX(i) + 0.5) * blockSize)
	blockField.vertices[(i * 2) + 1] = ((blocks.getY(i) + 0.5) * blockSize)

@window.event
def on_draw():

	for b in range(blocks.count):
		if blocks[b].dirty:
			blockField.colors[b * 4:(b * 4) + 3] = blocks[b].color1
			blocks[b].clean()
				
	window.clear()
	blockField.draw(pyglet.gl.GL_POINTS)

@window.event
def on_mouse_press(x, y, button, modifiers):
	if (x / 64 < blocks.width) and (y/64 < blocks.height) and x > 0 and y > 0:
		blocks[blocks.getListIndex(x/64,y/64)].color1 = [random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255)]


pyglet.app.run()

