#simple task list
import simplegui

tasks=[ ]

def clear():
    global tasks
    tasks=[]

    
def new(task):
    tasks.append(task)
    
    
def remove_num(tasknum):
    n=int(tasknum)
    if n>0 and n<=len(tasks):
        tasks.pop(n-1)
        
def remove_name(taskname):
    if taskname in tasks:
        tasks.remove(taskname)
        
def draw(canvas):
    h=25
    n=1
    for task in tasks:
        canvas.draw_text(str(n)+':'+task,[10,h*n],20,'white')
        n+=1
    
frame=simplegui.create_frame('task list',600,400)
frame.add_input('new task',new,200)
frame.add_input('remove task number',remove_num,200)
frame.add_input('remove task',remove_name,200)
frame.add_button('clear all',clear)

frame.set_draw_handler(draw)

frame.start()