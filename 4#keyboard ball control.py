#keyboard ball control
import simplegui

width=600
height=400
ball_radius=20
vel=[0,0]

ball_pos=[width/2,height/2]

def draw(canvas):
    ball_pos[0]+=vel[0]
    ball_pos[1]+=vel[1]
    
    canvas.draw_circle(ball_pos,ball_radius,2,'red','white')
    
    
def keydown(key):
    acc=1
    if key==simplegui.KEY_MAP["left"]:
        vel[0]-=acc
    elif key==simplegui.KEY_MAP["right"]:
        vel[0]+=acc
    elif key==simplegui.KEY_MAP["down"]:
        vel[1]+=acc
    elif key==simplegui.KEY_MAP["up"]:
        vel[1]-=acc
        
frame=simplegui.create_frame('Positional ball control',width,height)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

frame.start()