#Stopwatch 当毫秒数为零时得一分
import simplegui

counter = 0#总时间单位毫秒
point = 0#得分
subtry = 0#停止总次数
t = 0#秒表状态，0-停止，1-计数

def format(counter):
    tsecond = counter % 10
    second = ((counter - tsecond) % 600)/10
    minute = (counter - tsecond) // 600
    if second < 10:
        return str(minute)+':0'+str(second)+'.'+str(tsecond)
    else:
        return str(minute)+':'+str(second)+'.'+str(tsecond)
    
#format(0)    
#format(11) 
#format(321) 
#format(613) 
#format(55568) 

def tick():
    global counter
    counter += 1

def draw(canvas):
    canvas.draw_text(format(counter),[40,90],50,'white')
    canvas.draw_text(str(point)+'/'+str(subtry),[160,30],30,'yellow')

def start_handler():
    global t
    if t == 0:
        timer.start()
        t = 1

def stop_handler():
    global point,subtry,t
    if t == 1:
        timer.stop()
        subtry += 1
        if (counter % 10)==0 and counter != 0:
            point += 1
        t = 0

def reset_handler():
    global counter, point, subtry,t
    t=0
    counter=0
    point=0
    subtry=0
    timer.stop()
        

frame = simplegui.create_frame('Stopwatch',220,150)
timer = simplegui.create_timer(100,tick)

frame.add_button('Start',start_handler,100)
frame.add_button('Stop',stop_handler,100)
frame.add_button('Reset',reset_handler,100)
frame.set_draw_handler(draw)

frame.start()
