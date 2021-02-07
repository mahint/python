# Echo mouse click in console
import simplegui
###################################################
# Student should enter code below
WIDTH = 600
HEIGHT = 400
def click(pos):
    print pos
    
frame = simplegui.create_frame("Mouse Echo", WIDTH, HEIGHT)
frame.set_mouseclick_handler(click)

frame.start()
###################################################
# Sample output

#Mouse click at (104, 105)
#Mouse click at (169, 175)
#Mouse click at (197, 135)
#Mouse click at (176, 111)
#Mouse click at (121, 101)
#Mouse click at (166, 208)
#Mouse click at (257, 235)
#Mouse click at (255, 235)
