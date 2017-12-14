#add and remove ball
import simplegui
import math

width=450
height=300
#ball_pos = [width/2,height/2]
ball_color = 'red'
ball_list=[]
ball_radius=15

def dict(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

def click(pos):
    remove=[]
    for ball in ball_list:
        if dict(ball,pos)<ball_radius:
            remove.append(ball)

    if remove==[]:
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle(ball,ball_radius,1,'black',ball_color)
    
frame=simplegui.create_frame('mouse selection',width,height)
frame.set_canvas_background('white')

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()