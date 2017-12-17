#demo of animation using asteroid sprite sheet
import simplegui

rock_center = [64,64]
rock_size = [128,128]
rock_dim = 64
rock_image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png')

time = 0

def draw(canvas):
    global time
    current_rock_index = (time%rock_dim)//1
    current_rock_center = [rock_center[0]+current_rock_index *rock_size[0],rock_center[1]]
    canvas.draw_image(rock_image,current_rock_center,rock_size,rock_center,rock_size)
    time += 0.4#每秒0.4*60帧
    
frame = simplegui.create_frame('Asteroid sprite',rock_size[0],rock_size[1])

frame.set_draw_handler(draw)
frame.set_canvas_background('green')

frame.start()