# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 50
CARD_HEIGHT = 100
FONT_SIZE = 1

CARD1_WIDTH = 50

CARD2_WIDTH = 50
CARD2_WIDTH_2 = CARD_WIDTH*2 #100

CARD3_WIDTH = CARD_WIDTH*2 #100
CARD3_WIDTH_2 = CARD_WIDTH*3 #150

CARD4_WIDTH = CARD_WIDTH*3 #150
CARD4_WIDTH_2 = CARD_WIDTH*4 #200

CARD5_WIDTH = CARD_WIDTH*4
CARD5_WIDTH_2 = CARD_WIDTH*5 

CARD6_WIDTH = CARD_WIDTH*5
CARD6_WIDTH_2 = CARD_WIDTH*6

CARD7_WIDTH = CARD_WIDTH*6
CARD7_WIDTH_2 = CARD_WIDTH*7

CARD8_WIDTH = CARD_WIDTH*7
CARD8_WIDTH_2 = CARD_WIDTH*8

CARD9_WIDTH = CARD_WIDTH*8
CARD9_WIDTH_2 = CARD_WIDTH*9

CARD10_WIDTH = CARD_WIDTH*9
CARD10_WIDTH_2 = CARD_WIDTH*10

CARD11_WIDTH = CARD_WIDTH*10
CARD11_WIDTH_2 = CARD_WIDTH*11

CARD12_WIDTH = CARD_WIDTH*11
CARD12_WIDTH_2 = CARD_WIDTH*12

CARD13_WIDTH = CARD_WIDTH*12
CARD13_WIDTH_2 = CARD_WIDTH*13

CARD14_WIDTH = CARD_WIDTH*13
CARD14_WIDTH_2 = CARD_WIDTH*14

CARD15_WIDTH = CARD_WIDTH*14
CARD15_WIDTH_2 = CARD_WIDTH*15

CARD16_WIDTH = CARD_WIDTH*15
CARD16_WIDTH_2 = CARD_WIDTH*16


list1_numbers = range(0, 8)
list2_numbers = range(0, 8)
cards = []

cards.extend(list1_numbers)
cards.extend(list2_numbers)


random.shuffle(cards)

exposed = []

#exposed.extend(list1_numbers)
#exposed.extend(list2_numbers)

print exposed

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    print("pos: " + str(pos))
    # add game state logic here
    global CARD1_WIDTH, CARD2_WIDTH, CARD2_WIDTH_2, CARD3_WIDTH, CARD3_WIDTH_2, CARD4_WIDTH, CARD4_WIDTH_2, CARD5_WIDTH, CARD5_WIDTH_2, CARD6_WIDTH, CARD6_WIDTH_2, CARD7_WIDTH, CARD7_WIDTH_2, CARD8_WIDTH, CARD8_WIDTH_2, CARD9_WIDTH, CARD9_WIDTH_2, CARD10_WIDTH, CARD10_WIDTH_2, CARD11_WIDTH, CARD11_WIDTH_2, CARD12_WIDTH, CARD12_WIDTH_2, CARD13_WIDTH, CARD13_WIDTH_2, CARD14_WIDTH, CARD14_WIDTH_2, CARD15_WIDTH, CARD15_WIDTH_2, CARD16_WIDTH, CARD16_WIDTH_2
    print("card pos: " + str(pos[0] // 50))
    CARD_WIDTH = 0
    #CARD2_WIDTH_2 = 0
    

def init_cards(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        #print(card_pos)
        canvas.draw_text(
            str(cards[card_index]), 
            [12 + card_pos, 65], 48, "White")
        
        #for the first card
        if(card_index == 0):            
            canvas.draw_polygon(
                [
                    [0, 0], [CARD1_WIDTH, 0], 
                    [CARD1_WIDTH, CARD_HEIGHT], [0, CARD_HEIGHT]
                ], FONT_SIZE, "Red", "Green"
            )
        #for rest of the cards
        else:
            canvas.draw_polygon(
                [
                    [CARD_WIDTH*(card_index), 0], [CARD_WIDTH*(card_index+1), 0], 
                    [CARD_WIDTH*(card_index+1), CARD_HEIGHT], [CARD_WIDTH*(card_index), CARD_HEIGHT]
                ], FONT_SIZE, "Red", "Green"
            )

def draw(canvas):
    init_cards(canvas)
    #for exposed_index in exposed:
        #if exposed_index == 
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
