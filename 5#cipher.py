#cipher
import simplegui
import random

CIPHER={}
message=''
LETTERS='abcdefghijklmnopqrstuvwxyz'

def init():
    letter_list=list(LETTERS)
    random.shuffle(letter_list)
    for ch in LETTERS:
        CIPHER[ch]=letter_list.pop()

def encode():
    emsg=''
    for ch in message:
        emsg+=CIPHER[ch]
    print message,'encode to',emsg
    
    
def decode():
    dmsg=''
    for ch in message:
        for key in CIPHER:
            if ch == CIPHER[key]:
                dmsg+=key
    print message,'decode to',dmsg

def newmsg(msg):
    global message
    message=msg
    label.set_text(msg)
    
frame=simplegui.create_frame('Cipher',2,200,200)
frame.add_input('Message',newmsg,200)
label=frame.add_label('',200)
frame.add_button('encode',encode)
frame.add_button('decode',decode)
init()

frame.start()