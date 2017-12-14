import simplegui
import random

width=600
height=400
ball_radius=20
pad_width=8
pad_height=80

pad1_pos=height/2
pad2_pos=height/2
dir1=0
dir2=0
pad1_vel=5
pad2_vel=5

ball_pos = [width/2,height/2]
ball_vel = [0,0]

score1=0
score2=0
hit=0

left = False
right = True

def spawn_ball(direction):
    global ball_pos,ball_vel,hit
    hit=0
    ball_pos=[width/2,height/2]
    x=random.randrange(120,240)
    y=random.randrange(60,180)
    ball_vel[1] =-y/60
    if direction:
        ball_vel[0] =x/60
    else:
        ball_vel[0] =-x/60
    
def new_game():
    global pad1_pos,pad2_pos
    global score1,score2
    pad1_pos = height/2
    pad2_pos = height/2
    score1 = 0
    score2 = 0
    spawn_ball(random.randrange(0,2))       

def keydown(key):
    global pad1_pos,dir1,dir2
    if key==simplegui.KEY_MAP["w"]:
        dir1=-1
    elif key==simplegui.KEY_MAP["s"]:
        dir1=1
    elif key==simplegui.KEY_MAP["up"]:
        dir2=-1
    elif key==simplegui.KEY_MAP["down"]:
        dir2=1

def keyup(key):
    global pad2_pos,dir1,dir2
    if key==simplegui.KEY_MAP["w"] and dir1==-1:
        dir1=0
    elif key==simplegui.KEY_MAP["s"] and dir1==1:
        dir1=0
    elif key==simplegui.KEY_MAP["up"] and dir2==-1:
        dir2=0
    elif key==simplegui.KEY_MAP["down"] and dir2==1:
        dir2=0
        
def draw(c):
    global score1,score2,pad1_pos,pad2_pos,ball_pos,hit
    
    
    #draw mid line and gutters
    c.draw_line([width/2,0],[width/2,height],1,'white')
    c.draw_line([pad_width,0],[pad_width,height],1,'white')
    c.draw_line([width-pad_width,0],[width-pad_width,height],1,'white')
    
    #update ball
    ball_pos[0]+=ball_vel[0]*1.1**hit
    ball_pos[1]+=ball_vel[1]*1.1**hit

    if ball_pos[0] <= ball_radius+pad_width: 
        if ball_pos[1] >=pad1_pos-pad_height/2 and ball_pos[1] <=pad1_pos+pad_height/2:
            ball_vel[0]=-ball_vel[0]
            hit+=1
        else:
            score2+=1
            spawn_ball(right)
    if ball_pos[0] >= width-1-ball_radius-pad_width: 
        if ball_pos[1] >=pad2_pos-pad_height/2 and ball_pos[1] <=pad2_pos+pad_height/2:
            ball_vel[0]=-ball_vel[0]
            hit+=1
        else:
            score1+=1
            spawn_ball(left)            
    if ball_pos[1] <= ball_radius or ball_pos[1] >= height-1-ball_radius:
        ball_vel[1]=-ball_vel[1]
    
    #draw ball
    c.draw_circle(ball_pos,ball_radius,1,'white','white')
    
    #update paddle's vertical position
    if pad1_pos < pad_height/2:
        pad1_pos = pad_height/2
    elif pad1_pos > (height-pad_height/2):
        pad1_pos = (height-pad_height/2)    
    elif pad1_pos <= (height-pad_height/2) and pad1_pos >= (pad_height/2):
        pad1_pos=pad1_pos+dir1*pad1_vel
    
    #keep paddle on the screen    
    if pad2_pos < pad_height/2:
        pad2_pos = pad_height/2
    elif pad2_pos > (height-pad_height/2):
        pad2_pos = (height-pad_height/2)    
    elif pad2_pos <= (height-pad_height/2) and pad2_pos >= (pad_height/2):
        pad2_pos=pad2_pos+dir2*pad2_vel
        
    #draw paddles
    c.draw_line([pad_width/2,pad1_pos-pad_height/2],[pad_width/2,pad1_pos+pad_height/2],pad_width,'white')
    c.draw_line([width-pad_width/2,pad2_pos-pad_height/2],[width-pad_width/2,pad2_pos+pad_height/2],pad_width,'white')
    
    #draw socres
    c.draw_text(str(score1),[240,50],60,'white')
    c.draw_text(str(score2),[330,50],60,'white')
        
frame=simplegui.create_frame('Pong',width,height)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart',new_game,100)

new_game()
frame.start()