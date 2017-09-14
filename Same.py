import pyglet
import Block
import random

window = pyglet.window.Window()

blockVertices = [	100, 100, 100, 400,
					500, 400, 500, 100]

blockColors = [	0x00, 0xFF, 0xFF,
				0x00, 0xFF, 0xFF]

flag = pyglet.graphics.vertex_list(4, 'v2f', 'c3B')
flag.vertices = blockVertices
flag.colors = blockColors + blockColors

pyglet.gl.glPointSize(10.0)

blocksX = 6
blocksY = 5

blocks = [None] * blocksX


blockField = pyglet.graphics.vertex_list(blocksX * blocksY, 'v2f', 'c3B')
blockField.vertices = [0.0] * (blocksX * blocksY * 2)
blockField.colors = [0xFF] * (blocksX * blocksY * 3)

index = 0
for x in range(blocksX):
	blocks[x] = [None] * blocksY
	for y in range(blocksY):
		blocks[x][y] = Block.Block()
		blockField.vertices[index] = ((x * 100.0) + 50.0)
		blockField.vertices[index+1] = ((y * 100.0) + 50.0)
		index += 2


@window.event
def on_draw():

	for x in range(blocksX):
		for y in range(blocksY):
			if blocks[x][y].dirty:
				blockField.colors[(((blocksY * x) + y) * 3):(((blocksY * x) + y) * 3) + 3] = blocks[x][y].color
				blocks[x][y].clean()
				
	window.clear()
	blockField.draw(pyglet.gl.GL_POINTS)

@window.event
def on_mouse_press(x, y, button, modifiers):
	if (x / 100 < blocksX) and (y/100 < blocksY) and x > 0 and y > 0:
		blocks[x/100][y/100].color = [random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255)]


pyglet.app.run()

