#example of mouse input 2
import simplegui
import math

width=450
height=300
#ball_pos = [width/2,height/2]
#ball_color = 'red'
ball_list=[]
ball_radius=15

def dict(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

def click(pos):
    changed=False
    for ball in ball_list:
        if dict([ball[0],ball[1]],pos)<ball_radius:
            ball[2]='green'
            changed = True

    if not changed:
        ball_list.append([pos[0],pos[1],'red'])

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0],ball[1]],ball_radius,1,'black',ball[2])
    
frame=simplegui.create_frame('mouse selection',width,height)
frame.set_canvas_background('white')

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()