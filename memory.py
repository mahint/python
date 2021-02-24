# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 50
CARD_HEIGHT = 100

list1_numbers = range(0, 8)
list2_numbers = range(0, 8)
cards = []

cards.extend(list1_numbers)
cards.extend(list2_numbers)

print cards

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_text(str(cards[card_index]), (0, card_pos), 48, "Green")
    
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
