#Memory

import simplegui
import random

cwidth = 50
cheight = 100
turn = 0
state = 0
number = '0011223344556677'
num_list = ''
card_list = range(0,16)
click_list = []

#helper function to initiation globals
def new_game():
    global turn,state,num_list,click_list,card_list
    num_list = list(number)
    random.shuffle(num_list)
    card_list = range(0,16)
    click_list = []
    turn = 0
    state = 0

def mouseclick(pos):
    global click_list,state,turn
    a = pos[0]//cwidth
    if state == 0:
        click_list.append(a)
        state = 1
    elif state == 1:
        if a in card_list:
            click_list.append(a)
            state = 2
            turn += 1
    else:
        if a in card_list:
            if num_list[click_list[-1]] != num_list[click_list[-2]]:
                click_list.pop()
                click_list.pop()
            click_list.append(a)
            state=1
                            
#cards are logically 50x100 pixels in size
def draw(canvas):
    global card_list
    card_list = list(range(0,16))
    for i in click_list:
        if i in card_list:
            card_list.remove(i)
        
    #draw numbers
    for i in range(0,16):
        canvas.draw_text(num_list[i],[i*cwidth+cwidth/3,cheight*2/3],cheight/3,'white')
                
    #draw lines
    for i in range(0,17):
        canvas.draw_line([i*cwidth,0],[i*cwidth,cheight],2,'white')
        
    canvas.draw_line([0,0],[cwidth*16,0],2,'white')
    canvas.draw_line([0,cheight],[cwidth*16,cheight],2,'white')
    
    #draw cards
    for i in card_list:
        canvas.draw_line([i*cwidth+cwidth/2,1],[i*cwidth+cwidth/2,cheight-1],cwidth-4,'green')
    
    #draw label
    l.set_text("Turns = "+str(turn))  

frame = simplegui.create_frame('memory',800,100)
frame.add_button('restart',new_game)
l=frame.add_label('Turns = 0')

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()