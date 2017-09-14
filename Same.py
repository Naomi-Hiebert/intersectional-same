import pyglet

window = pyglet.window.Window()

blockVertices = [	100, 100, 100, 400, 500, 100,
					100, 400, 500, 100, 500, 400]

blockColors = [	0x00, 0xFF, 0xFF,
				0x00, 0xFF, 0xFF]

flag = pyglet.graphics.vertex_list(6, 'v2f', 'c3B')
flag.vertices = blockVertices
flag.colors = blockColors + blockColors + blockColors

clickCount = 0


@window.event
def on_draw():
	window.clear()
	flag.draw(pyglet.gl.GL_TRIANGLES)

@window.event
def on_mouse_press(x, y, button, modifiers):
	global clickCount

	if clickCount >= 8:
		clickCount = 0

	newColor = [0xFF, 0x00, 0xFF]
	if clickCount >= 4:
		newColor = [0x00, 0xFF, 0xFF]

	if clickCount % 4 == 0:
		flag.colors[0:3] = newColor
	elif clickCount % 4 == 1:
		flag.colors[3:6] = newColor
		flag.colors[9:12] = newColor
	elif clickCount % 4 == 2:
		flag.colors[6:9] = newColor
		flag.colors[12:15] = newColor
	else:
		flag.colors[15:18] = newColor

	clickCount += 1


pyglet.app.run()

