#Ball physics object oriented
import simplegui
import random
import math

width = 600
height = 400
radius = 20
color = 'white'

def dot(v,w):
    return v[0]*w[0]+v[1]*w[1]

class rectangulardomain:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def inside(self,center,radius):
        return radius<=center[0]<=self.width-radius and radius<=center[1]<=self.height-radius
        
    def normal(self,center):
        a = center[0]
        b = center[1]
        c = self.width-center[0]
        d = self.height-center[1]
        if a<=b and a<=c and a<=d:
            return [-1,0]
        elif b<=a and b<=c and b<=d:
            return [0,-1]
        elif c<=a and c<=b and c<=d:
            return [1,0]
        else:
            return [0,1]
        
    def random_pos(self,radius):
        pos = []
        x = random.randrange(radius,self.width-radius)
        y = random.randrange(radius,self.height-radius)
        pos.append(x)
        pos.append(y)
        return pos
        
    def draw(self,canvas):
        canvas.draw_line([0,0],[0,self.height],3,'red')
        canvas.draw_line([0,0],[self.width,0],3,'red')
        canvas.draw_line([self.width,0],[self.width,self.height],3,'red')
        canvas.draw_line([0,self.height],[self.width,self.height],3,'red')
    
class circledomain:
    def __init__(self,pos,Radius):
        self.pos = pos
        self.Radius = Radius
        
    def inside(self,center,radius):
        return (center[0]-self.pos[0])**2+(center[1]-self.pos[1])**2 <= (self.Radius-radius)**2
        
    def normal(self,center):
        nor = []
        a = center[0]-self.pos[0]
        b = center[1]-self.pos[1]
        l = math.sqrt(a**2+b**2)
        nor.append(a/l)
        nor.append(b/l)
        return nor
        
        
    def random_pos(self,radius):
        pos = []
        d = random.randrange(0,360)
        r = random.randrange(0,self.Radius-radius)
        pos.append(r*math.cos(d)+self.pos[0])
        pos.append(r*math.sin(d)+self.pos[1])
        return pos
        
    def draw(self,canvas):
        canvas.draw_circle(self.pos,self.Radius,3,'red')

class Ball:
    def __init__(self,radius,color,domain):
        self.radius = radius
        self.color = color
        self.domain = domain
        
        self.pos = self.domain.random_pos(self.radius)
        self.vel = [random.random() + .1,random.random() + .1]
        
    def reflect(self):
        norm = self.domain.normal(self.pos)
        norm_length = dot(self.vel,norm)
        self.vel[0] = self.vel[0] - 2 * norm_length * norm[0]
        self.vel[1] = self.vel[1] - 2 * norm_length * norm[1]
            
            
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if not self.domain.inside(self.pos,self.radius):
            self.reflect()
                
    def draw(self,canvas):
        canvas.draw_circle(self.pos,self.radius,1,
                               self.color,self.color)
            
            
def draw(canvas):
    ball.update()
    field.draw(canvas)
    ball.draw(canvas)
    
#field = rectangulardomain(width,height)
field = circledomain([width/2,height/2],180)
ball = Ball(radius,color,field)

frame = simplegui.create_frame('ball physics',width,height)
frame.set_draw_handler(draw)
frame.start()