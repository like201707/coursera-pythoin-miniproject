# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_card = []

    def __str__(self):
        a = ""
        for card in self.hand_card:
            a += card.get_suit() + card.get_rank() + " "
        return "Hand contains %s " %a

    def add_card(self, card):
        self.hand_card.append(card)

    def get_value(self):
        value = 0
        Num_A = 0
        for i in range(len(self.hand_card)):
            value += VALUES[self.hand_card[i].get_rank()]
            if self.hand_card[i].get_rank() == 'A':
                Num_A += 1
            else:
                pass
        for i in range(Num_A):
            if value + 10 <= 21:
                value += 10
        return value 

    def draw(self, canvas, pos):
        for i in range(len(self.hand_card)):
            self.hand_card[i].draw(canvas,[pos[0]+i*CARD_SIZE[0],pos[1]])
           


 
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.card_deck.append(Card(suit,rank))
                

    def shuffle(self):
        return random.shuffle(self.card_deck) 


    def deal_card(self):
        return self.card_deck.pop()
    
    def __str__(self):
        b = ""
        for card in self.card_deck:
            b += card.get_suit() + card.get_rank() + " "
        return "Deck contains %s" %b 
        



#define event handlers for buttons
def deal():
    global outcome, in_play
    global player, dealer, newdeck
    player = Hand()
    dealer = Hand()
    newdeck = Deck()
    newdeck.shuffle()
    player.add_card(newdeck.deal_card())
    player.add_card(newdeck.deal_card())
    dealer.add_card(newdeck.deal_card())
    dealer.add_card(newdeck.deal_card())
    in_play = True

def hit():
    global player, newdeck , in_play ,score
    if player.get_value() <= 21 and in_play:
        player.add_card(newdeck.deal_card()) 
    if player.get_value() > 21:  
        print player.get_value(), "You have busted"
        in_play = False
        score += -1
    
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer, player, newdeck,score, in_play
    while dealer.get_value() <= 17:
        dealer.add_card(newdeck.deal_card())
    if dealer.get_value() > 21:
        score += 1
    elif player.get_value() > dealer.get_value():
        score += 1
    else:
        score -= 1

    in_play = False
        
    
   


# draw handler    
def draw(canvas):
    player.draw(canvas, [200, 300])
    dealer.draw(canvas, [200, 100])
    canvas.draw_text("Blackjack",[250,550],45, "Black")
    canvas.draw_text("Player",[50,350],45, "Black")
    canvas.draw_text("Dealer",[50,150],45, "Black")
    canvas.draw_text("SCORE: " + str(score), [250,50],45,"Red")
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [200+CARD_CENTER[0], 100+CARD_CENTER[1]] ,CARD_SIZE)
        canvas.draw_text("Hit or Stand ?", [250,250],45, "Red")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
