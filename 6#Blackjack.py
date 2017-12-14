#mini-project #6 - Blackjack

import simplegui
import random

#load card sprites - 949x392 - source: jfitz.com
card_size = (73,98)
card_center = (36.5,49)
card_image = simplegui.load_image('http://img.blog.csdn.net/20171211201100552?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbHlob3BlOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center')

card_back_size = (71,96)
card_back_center = (35.5,48)
card_back = simplegui.load_image('http://img.blog.csdn.net/20171211200638571?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbHlob3BlOQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center')

#initialize some useful global variables
in_play = False
outcome = ''
tip = 'Hit or stand?'
score = 0


#define globals for cards
suits = ('C','S','H','D')
ranks = ('A','2','3','4','5','6','7','8','9','T','J','Q','K')
values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
         'T':10,'J':10,'Q':10,'K':10}

#define card class
class Card:
    def __init__(self,suit,rank):
        if suit in suits and rank in ranks:
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print 'Invalid card: ',suit,rank
            
    def __str__(self):
        return self.suit + self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def draw(self,canvas,pos):
        card_loc = (card_center[0]+card_size[0]*ranks.index(self.rank),
                    card_center[1]+card_size[1]*suits.index(self.suit))
        canvas.draw_image(card_image,card_loc,card_size,[pos[0]+card_center[0],pos[1]+card_center[1]],card_size)


#define hand class
class Hand:
    def __init__(self):
        self.hand = []
        
    def __str__(self):
        s='Hand contains '  # return a string representing the deck  
        if len(self.hand)==0:  
            return s  
        for tmp in self.hand:  
            s+=str(tmp)+' '  
        return s 
    
    def add_card(self,card):
        self.card = card
        self.hand.append(self.card)
    
    def get_value(self):
        sub = 0
        ace = 0
        for card in self.hand:
            sub += values[card.get_rank()]
            if card.get_rank() == 'A':
                ace = 1
        if ace == 0:
            return sub
        else:
            if sub+10<=21:
                return sub+10
            else:
                return sub
    
    def busted(self):
        pass
    
    def draw(self,canvas,p):
        n = len(self.hand)
        if n >0:
            for i in range(0,n):
                self.hand[i].draw(canvas,p)
                p[0] += 100
            
#define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))
                    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_card(self):
        a = self.deck.pop(0)
        return a
        #print 'The Deck is Empty'
    
    def __str__(self):  
        s='Deck contains '  # return a string representing the deck  
        if len(self.deck)==0:  
            return s  
        for tmp in self.deck:  
            s+=tmp.__str__()+' '  
        return s  
    
def deal():
    global outcome,tip,in_play,deck,player,dealer,score
    if in_play:
        outcome = 'You lose.'
        tip = 'New deal?'
        score -= 1
        in_play = False
    else:    
        in_play = True
        outcome = ''
        tip = 'Hit or stand?'
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
                     
def hit():
    global player,outcome,tip,in_play,score
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = 'You went bust and lose.'
            tip = 'New deal?'
            in_play = False
            score -= 1

def stand():
    global in_play,outcome,tip,dealer,score
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() <= player.get_value() or dealer.get_value() > 21:
            outcome = 'You win.'
            score += 1
        else:
            outcome = 'You lose.'
            score -= 1
        in_play = False
    
    tip = 'New deal?'
                    
def draw(canvas):
    player.draw(canvas,[70,350])
    dealer.draw(canvas,[70,150])
    canvas.draw_text(tip,[220,320],30,'black')
    canvas.draw_text(outcome,[220,120],30,'black')
    canvas.draw_text('Player',[70,320],30,'black')
    canvas.draw_text('Dealer',[70,120],30,'black')
    canvas.draw_text('Blackjack',[80,70],50,'blue')
    canvas.draw_text('Score '+str(score),[420,70],30,'black')
    if in_play:
        canvas.draw_image(card_back,card_back_center,card_back_size,[70+card_center[0],150+card_center[1]],card_back_size)


#################                    
frame = simplegui.create_frame('blackjack',600,500)
frame.set_canvas_background('green')
                    
frame.add_button('Deal',deal,200)
frame.add_button('Hit',hit,200)
frame.add_button('stand',stand,200)
frame.set_draw_handler(draw)

deck = Deck()
player = Hand()
dealer = Hand()
deal()

frame.start()





