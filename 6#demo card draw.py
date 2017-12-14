#demo card draw
import simplegui

#define globals for cards
ranks = ('A','2','3','4','5','6','7','8','9','T','J','Q','K')
suits = ('C','S','H','D')

#card sprite - 950x392
card_center = (36.5,49)
card_size = (73,98)
#card_image = simplegui.load_image('http://s6.sinaimg.cn/orignal/4f13528e44cce7b9ff5a5&690')
card_image = simplegui.load_image('http://img.blog.csdn.net/20171211201100552?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbHlob3BlOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center')


#define card class
class card:
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
    
    def draw(self,canvas,loc):
        i = ranks.index(self.rank)
        j = suits.index(self.suit)
        card_pos = [card_center[0]+i*card_size[0],
                    card_center[1]+j*card_size[1]]
        canvas.draw_image(card_image,card_pos,card_size,loc,card_size)
        
#define draw handler
def draw(canvas):
    one_card.draw(canvas,(155,90))
    
    
#define frame and register draw handler
frame = simplegui.create_frame('card draw',300,200)
frame.set_draw_handler(draw)

one_card = card('C','A')

frame.start()