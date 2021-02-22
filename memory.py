# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 100
CARD_HEIGHT = 50

list1_numbers = range(0, 8)
list2_numbers = range(0, 8)
lists = []

lists.extend(list1_numbers)
lists.extend(list2_numbers)

print lists

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    canvas.draw_polygon([[0, 0], [0, CARD_WIDTH], [0, CARD_HEIGHT]], CARD_WIDTH, "Green") 
    
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
