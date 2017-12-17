#animation of explosion using 2D sprite sheet
import simplegui

explosion_center = [50,50]
explosion_size = [100,100]
explosion_dim = [9,9]
explosion_image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png')


time = 0

def draw(canvas):
    global time
    explosion_index = [time % explosion_dim[0],(time//explosion_dim[0]) % explosion_dim[1]]
    canvas.draw_image(explosion_image,
                      [explosion_center[0]+explosion_index[0] *explosion_size[0],
                      explosion_center[1]+explosion_index[1] *explosion_size[1]],
                      explosion_size,explosion_center,explosion_size)
    time += 1
    
frame = simplegui.create_frame('Asteroid sprite',explosion_size[0],explosion_size[1])

frame.set_draw_handler(draw)
frame.set_canvas_background('green')

frame.start()