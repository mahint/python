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


random.shuffle(cards)

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
        canvas.draw_text(str(cards[card_index]), [12 + card_pos, 65], 48, "White")
        canvas.draw_polygon([[0, 0], [CARD_WIDTH, 0], [CARD_WIDTH, CARD_HEIGHT], [0, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[CARD_WIDTH, 0], [2*CARD_WIDTH, 0], [2*CARD_WIDTH, CARD_HEIGHT], [CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[2*CARD_WIDTH, 0], [3*CARD_WIDTH, 0], [3*CARD_WIDTH, CARD_HEIGHT], [2*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[3*CARD_WIDTH, 0], [4*CARD_WIDTH, 0], [4*CARD_WIDTH, CARD_HEIGHT], [3*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[4*CARD_WIDTH, 0], [5*CARD_WIDTH, 0], [5*CARD_WIDTH, CARD_HEIGHT], [4*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[5*CARD_WIDTH, 0], [6*CARD_WIDTH, 0], [6*CARD_WIDTH, CARD_HEIGHT], [5*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[6*CARD_WIDTH, 0], [7*CARD_WIDTH, 0], [7*CARD_WIDTH, CARD_HEIGHT], [6*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[7*CARD_WIDTH, 0], [8*CARD_WIDTH, 0], [8*CARD_WIDTH, CARD_HEIGHT], [7*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[8*CARD_WIDTH, 0], [9*CARD_WIDTH, 0], [9*CARD_WIDTH, CARD_HEIGHT], [8*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[9*CARD_WIDTH, 0], [10*CARD_WIDTH, 0], [10*CARD_WIDTH, CARD_HEIGHT], [9*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[10*CARD_WIDTH, 0], [11*CARD_WIDTH, 0], [11*CARD_WIDTH, CARD_HEIGHT], [10*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[11*CARD_WIDTH, 0], [12*CARD_WIDTH, 0], [12*CARD_WIDTH, CARD_HEIGHT], [11*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[12*CARD_WIDTH, 0], [13*CARD_WIDTH, 0], [13*CARD_WIDTH, CARD_HEIGHT], [12*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[13*CARD_WIDTH, 0], [14*CARD_WIDTH, 0], [14*CARD_WIDTH, CARD_HEIGHT], [13*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[14*CARD_WIDTH, 0], [15*CARD_WIDTH, 0], [15*CARD_WIDTH, CARD_HEIGHT], [14*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
        canvas.draw_polygon([[15*CARD_WIDTH, 0], [16*CARD_WIDTH, 0], [16*CARD_WIDTH, CARD_HEIGHT], [15*CARD_WIDTH, CARD_HEIGHT]], 1, "Red", "Green")
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
