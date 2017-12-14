import simplegui
import random

position=[50,50]
message='python is fun!'
time=1000
width=400
height=400


def update(text):
    global message
    message=text
    
    
def tick():
    x=random.randrange(0,width)
    y=random.randrange(0,height)
    position[0]=x
    position[1]=y
    
    
def draw(canvas):
    canvas.draw_text(message,position,36,'red')
    
    
frame=simplegui.create_frame('Home',width,height)

frame.add_input('message:',update,100)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(time,tick)
    
frame.start()
timer.start()
    