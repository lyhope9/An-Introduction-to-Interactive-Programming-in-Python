#ball physics
import simplegui

width=600
height=400
ball_radius=20
vel=[-40.0/60,5.0/60]
ball_pos=[width/2,height/2]

def draw(canvas):
    ball_pos[0]+=vel[0]
    ball_pos[1]+=vel[1]
    
    if ball_pos[0]<=ball_radius:
        vel[0]=-vel[0]
    elif ball_pos[0]>=(width-1)-ball_radius:
        vel[0]=-vel[0]
    elif ball_pos[1]<=ball_radius:
        vel[1]=-vel[1]
    elif ball_pos[1]>=(height-1)-ball_radius:
        vel[1]=-vel[1]
    
    canvas.draw_circle(ball_pos,ball_radius,2,'red','white')
    
frame=simplegui.create_frame('Ball physics',width,height)

frame.set_draw_handler(draw)

frame.start()
    
   