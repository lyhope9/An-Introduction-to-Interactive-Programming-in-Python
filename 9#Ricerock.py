#Ricerock
import simplegui
import random
import math

#globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0
started = False

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
#debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
debris_image = simplegui.load_image("http://img.blog.csdn.net/20171220180209600")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
#nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
nebula_image = simplegui.load_image("http://img.blog.csdn.net/20171220180303321")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
#splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
splash_image = simplegui.load_image("http://img.blog.csdn.net/20171220180347878")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
#ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
ship_image = simplegui.load_image("http://img.blog.csdn.net/20171220180225517")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
#missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_image = simplegui.load_image("http://img.blog.csdn.net/20171220180332309")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
#asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image = simplegui.load_image("http://img.blog.csdn.net/20171220180155410")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
#explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_image = simplegui.load_image("http://img.blog.csdn.net/20171220180249116")

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

def process_sprite_group(aset,canvas):
    for one in aset:
        one.draw(canvas)
    for one in set(aset):
        if one.update():
            aset.remove(one)

def group_collide(group,o_object):
    global explosion_group
    len1 = len(group)
    for one in set(group):
        if one.collide(o_object):
            group.remove(one)
            explosion_group.add(Sprite(one.pos,[0,0],0,0,explosion_image,explosion_info,explosion_sound ))
    return len1-len(group)

def group_group_collide(aset,bset):
    num = 0
    for oneb in bset:
        num += group_collide(aset,oneb)
    return num

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
        global missile_group
        mis_vel = dist(self.vel,[0,0])
        forward = angle_to_vector(self.angle)
        missile_group.add( Sprite([self.pos[0] + 43*forward[0],self.pos[1] + 43*forward[1]],
                               [(7+mis_vel)*forward[0],(7+mis_vel)*forward[1]],
                               self.angle,0,missile_image,missile_info,missile_sound) )
        
    def draw(self,canvas):           
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
           
            
    def update(self):    
        if self.thrust:
            acc = 0.1
            self.image_center[0] = 135            
            self.sound.play()
        else:
            acc = 0
            self.sound.rewind()
            self.image_center[0] = 45
            
        self.angle += self.angle_vel
        
        self.vel[0] *= (1-0.01)
        self.vel[1] *= (1-0.01)
        
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
   
    def collide(self,o_object):
        d = dist(self.pos,o_object.pos)
        r = self.radius + o_object.radius
        if d>r:
            return False
        else:
            return True

    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image,[ self.image_center[0]+self.age*self.image_size[0],self.image_center[1] ], 
                              self.image_size,self.pos, self.image_size,self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
    
    def update(self):
        self.age += 1
        self.angle += self.angle_vel
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % width
        self.pos[1] = self.pos[1] % height
        
        if self.age < self.lifespan:
            return False
        else:
            return True

        
def key_down(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -0.05
    elif key ==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0.05
    elif key ==simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    elif key ==simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        
def key_up(key):
    if my_ship.angle_vel == 0.05 and key ==simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0
    elif my_ship.angle_vel == -0.05 and key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False
        
def click(pos):
    global started, lives, score
    center = [width/2,height/2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0]/2) < pos[0] < (center[0] + size[0]/2)
    inheight = (center[1] - size[1]/2) < pos[1] < (center[1] + size[1]/2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        soundtrack.rewind()
        soundtrack.play()
    
def draw(canvas):
    global time, score, lives, started, rock_group

    # animiate background
    time += 1
    wtime = (time / 4) % width
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width / 2, height / 2], [width, height])
    canvas.draw_image(debris_image, center, size, (wtime - width / 2, height / 2), (width, height))
    canvas.draw_image(debris_image, center, size, (wtime + width / 2, height / 2), (width, height))

    #draw lives and score
    canvas.draw_text('Lives',[70,70],30,'White')
    canvas.draw_text(str(lives),[70,110],30,'White')
    canvas.draw_text('Score',[670,70],30,'White')
    canvas.draw_text(str(score),[670,110],30,'White')
    
    #draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group,canvas)
    process_sprite_group(missile_group,canvas)
    process_sprite_group(explosion_group,canvas)
    
    #update ship and sprites
    my_ship.update()
    
    #detect collide
    hurt = group_collide(rock_group,my_ship)
    lives -= hurt
    
    goal = group_group_collide(rock_group,missile_group)
    score += goal
    
    #draw splash screen if not started
    if lives == 0:
        started = False
    if not started:
        canvas.draw_image(splash_image,splash_info.get_center(),
                         splash_info.get_size(),[width/2,height/2],
                         splash_info.get_size())
        rock_group = set([])

def rock_spawner():
    global rock_group
    level = 0.6 + score//8
    if started:
        if len(rock_group) < 12:
            rock_pos = [random.randrange(0,width),random.randrange(0,height)]
            rock_vel = [random.random()*level-level/2,random.random()*level-level/2]
            rock_avel = random.random()*0.2-0.1
            a_rock = Sprite(rock_pos,rock_vel,0,rock_avel,asteroid_image,asteroid_info)
            if dist(a_rock.pos, my_ship.pos) > 2.5 * my_ship.radius:
                rock_group.add(a_rock)
            else:
                rock_spawner()

#initialize frame
frame = simplegui.create_frame('Asteroids',width,height)

#initialize ship and two sprites
rock_group = set([])
missile_group = set([])
explosion_group = set([])
my_ship = Ship([width/2,height/2],[0,0],0,ship_image,ship_info,ship_thrust_sound)
#rock_group.add( Sprite([width/3,height/3],[1,1],0,0,asteroid_image,asteroid_info) )
#a_missile.add( Sprite([width*2/3,height*2/3],[-1,1],0,0,missile_image,missile_info,missile_sound) )


#register handler
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0,rock_spawner)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(click)

#get things rolling
timer.start()
frame.start()
