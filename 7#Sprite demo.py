#Sprite demo
import simplegui
import math

class ImageInfo:
    def __init__(self,center,size,radius = 0,lifespan = None,animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
        
    def get_center(self):
        return self.center
    
    def get_size(self):
        return self.size
    
    def get_radius(self):
        return self.radius
    
    def get_lifespan(self):
        return self.lifespan
    
    def get_animated(self):
        return self.animated
    
#load ship image
asteroid_info = ImageInfo([45,45],[90,90],40)
asteroid_image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png')


class Sprite():
    def __init__(self,pos,vel,ang,ang_vel,image,info,sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            
    def draw(self,canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
        #canvas.draw_circle(self.pos,self.radius,1,'red','red')
        
        
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
    
def draw(canvas):
    a_rock.draw(canvas)
    a_rock.update()

frame = simplegui.create_frame('Sprite demo',800,600)

a_rock = Sprite([400,300],[0.8,0.6],0,0.05,asteroid_image,asteroid_info)

frame.set_draw_handler(draw)

frame.start()
    
    
        
        
