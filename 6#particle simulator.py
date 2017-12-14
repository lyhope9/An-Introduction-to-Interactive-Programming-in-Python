#particle simulator
import simplegui
import random

width = 600
height = 400

particle_radius = 5
color_list = ['red','green','yellow','blue','white']
direction_list = [[1,0],[0,1],[-1,0],[0,-1]]

class particle:
    def __init__(self,position,color):
        self.position = position
        self.color = color
        
    def move(self,offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
            
    def draw(self,canvas):
        canvas.draw_circle(self.position,particle_radius,1,self.color,self.color)
                           
    def __str__(self):
        return 'particle with position = '+str(self.position)+' and color = '+self.color


def draw(canvas):
    for p in particle_list:
        p.move(random.choice(direction_list))
        
    for p in particle_list:
        p.draw(canvas)
        

frame = simplegui.create_frame('particle simulator',width,height)
frame.set_draw_handler(draw)

particle_list = []
for i in range(100):
    p = particle([width/2,height/2],random.choice(color_list))
    particle_list.append(p)
    print(p)
                  
frame.start()