#example of mouse input
import simplegui
import math

width=600
height=400
ball_pos = [width/2,height/2]
ball_color = 'red'
ball_radius=20

def dict(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

def click(pos):
    global ball_pos,ball_color
    if dict(pos,ball_pos)<ball_radius:
        ball_color='green'
    else:
        ball_pos=pos
        ball_color='red'

def draw(canvas):
    canvas.draw_circle(ball_pos,ball_radius,1,'black',ball_color)
    
frame=simplegui.create_frame('mouse selection',width,height)
frame.set_canvas_background('white')

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()