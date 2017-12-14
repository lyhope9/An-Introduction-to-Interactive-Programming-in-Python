import simplegui

def play():
    music.play()

def pause():
    music.pause()

def rewind():
    music.rewind()
    
def laugh():
    laugh.play()
    
def vol_down():
    global vol
    if vol >0:
        vol -= 1
    music.set_volume(vol/10.0)
    volume_button.set_text('volume = '+str(vol))
    
def vol_up():
    global vol
    if vol <10:
        vol += 1
    music.set_volume(vol/10.0)
    volume_button.set_text('volume = '+str(vol))
    
def play():
    music.play()

frame = simplegui.create_frame('Music demo',250,250,100)

frame.add_button('play',play,100)
frame.add_button('pause',pause,100)
frame.add_button('rewind',rewind,100)
frame.add_button('laugh',laugh,100)
frame.add_button('vol down',vol_down,100)
frame.add_button('vol up',vol_up,100)

vol = 7
volume_button = frame.add_label('volume = '+str(vol))


music = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
laugh = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg')

laugh.set_volume(.1)

frame.start()


