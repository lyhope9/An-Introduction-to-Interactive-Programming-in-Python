#Mini project Spaceship
import simplegui
import random
import math

#globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
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
    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

#helper function to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang),math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


#ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, sound):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = sound
    
    def shoot(self):
        global a_missile
        mis_vel = dist(self.vel,[0,0])
        a_missile.pos[0] = self.pos[0] + 43*angle_to_vector(self.angle)[0]
        a_missile.pos[1] = self.pos[1] + 43*angle_to_vector(self.angle)[1]
        a_missile.vel[0] = (7+mis_vel)*angle_to_vector(self.angle)[0]
        a_missile.vel[1] = (7+mis_vel)*angle_to_vector(self.angle)[1]
        a_missile = Sprite(a_missile.pos,a_missile.vel,0,0,missile_image,missile_info,missile_sound)


        
    def draw(self,canvas):           
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
           
            
    def update(self):    
        if self.thrust:
            acc = 0.4
            self.image_center[0] = 135            
            self.sound.play()
        else:
            acc = 0
            self.sound.rewind()
            self.image_center[0] = 45
            
        self.angle += self.angle_vel
        
        self.vel[0] *= (1-0.03)
        self.vel[1] *= (1-0.03)
        
        self.vel[0] =self.vel[0] + acc * angle_to_vector(self.angle)[0]
        self.vel[1] =self.vel[1] + acc * angle_to_vector(self.angle)[1]
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % width
        self.pos[1] = self.pos[1] % height
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
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
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % width
        self.pos[1] = self.pos[1] % height        

def key_down(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -0.03
    elif key ==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0.03
    elif key ==simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    elif key ==simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        
def key_up(key):
    if my_ship.angle_vel == 0.03 and key ==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0
    elif my_ship.angle_vel == -0.03 and key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False
    
def draw(canvas):
    global time,score,lives
    
    #animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time/8)%center[0]
    canvas.draw_image(nebula_image,nebula_info.get_center(),nebula_info.get_size(),[width/2,height/2],[width,height])
    canvas.draw_image(debris_image,[center[0]-wtime,center[1]],[size[0]-2*wtime,size[1]],
                      [width/2+1.25*wtime,height/2],[width-2.5*wtime,height])
    
    #draw lives and score
    canvas.draw_text('Lives',[70,70],30,'White')
    canvas.draw_text(str(lives),[70,110],30,'White')
    canvas.draw_text('Score',[670,70],30,'White')
    canvas.draw_text(str(score),[670,110],30,'White')
    
    #draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    #update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()


def rock_spawner():
    global a_rock
    Dir = ([1,1],[1,-1],[-1,1],[-1,-1])
    
    a_rock.pos[0] = random.randrange(0,width)
    a_rock.pos[1] = random.randrange(0,height)
    a_rock.vel[0] = (random.randrange(50,100)) / 20.0
    a_rock.vel[0] = (random.randrange(50,100)) / 20.0
    dir = random.choice(Dir)
    a_rock.vel[0] *= dir[0]
    a_rock.vel[1] *= dir[1]
    a_rock.angle = (random.randrange(-300,300)) / 10.0
    a_rock.angle_vel = (random.randrange(15,25)) / 200.0
    dir = random.choice(Dir)
    a_rock.angle_vel *= dir[0]
    
#initialize frame
frame = simplegui.create_frame('Asteroids',width,height)

#initialize ship and two sprites
my_ship = Ship([width/2,height/2],[0,0],0,ship_image,ship_info,ship_thrust_sound)
a_rock = Sprite([width/3,height/3],[1,1],0,0,asteroid_image,asteroid_info)
a_missile = Sprite([width*2/3,height*2/3],[-1,1],0,0,missile_image,missile_info,missile_sound)

rock_spawner()

#register handler
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0,rock_spawner)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

#get things rolling
timer.start()
frame.start()