import simplegui

size = 10
radius = 10

def button1_handler():
    global size
    size += 1
    label.set_text('value:'+str(size))

def button2_handler():
    global size
    if size > 1:
        size -= 1
        label.set_text('value:'+str(size))
    
def button3_handler():
    global radius
    radius = size
    label2.set_text('radius:'+str(radius))

def draw_handler(canvas):
    canvas.draw_circle([100,100],radius,5,'red')
        
frame=simplegui.create_frame("Home",200,200)
label = frame.add_label('value:'+str(size))
frame.add_button('increase',button1_handler,100)
frame.add_button('decrease',button2_handler,100)
label2 = frame.add_label('radius:'+str(radius))
frame.add_button('change circle',button3_handler,100)
frame.set_draw_handler(draw_handler)

frame.start()