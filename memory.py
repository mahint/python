  
# implementation of card game - Memory

import simplegui
import random
import math

CARD_WIDTH = 50
CARD_HEIGHT = 100
FONT_SIZE = 1

CARD1_WIDTH = 50

CARD2_WIDTH = 50
CARD2_WIDTH_2 = CARD_WIDTH*2

CARD3_WIDTH = CARD_WIDTH*2
CARD3_WIDTH_2 = CARD_WIDTH*3

CARD4_WIDTH = CARD_WIDTH*3
CARD4_WIDTH_2 = CARD_WIDTH*4

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

state = 0 



#exposed.extend(list2_numbers)

print exposed

# helper function to initialize globals
def new_game():
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global CARD1_WIDTH, CARD2_WIDTH, CARD2_WIDTH_2, CARD3_WIDTH, CARD3_WIDTH_2, CARD4_WIDTH, CARD4_WIDTH_2, CARD5_WIDTH, CARD5_WIDTH_2, CARD6_WIDTH, CARD6_WIDTH_2, CARD7_WIDTH, CARD7_WIDTH_2, CARD8_WIDTH, CARD8_WIDTH_2, CARD9_WIDTH, CARD9_WIDTH_2, CARD10_WIDTH, CARD10_WIDTH_2, CARD11_WIDTH, CARD11_WIDTH_2, CARD12_WIDTH, CARD12_WIDTH_2, CARD13_WIDTH, CARD13_WIDTH_2, CARD14_WIDTH, CARD14_WIDTH_2, CARD15_WIDTH, CARD15_WIDTH_2, CARD16_WIDTH, CARD16_WIDTH_2, exposed, state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    elif state == 2:
        state = 3
    elif state == 3:       
        state = 1
        
    print state
    
    #for number in cards:
        #if cards[0] == number:
            #CARD1_WIDTH = 0
    
            
    if pos[0] < CARD_WIDTH:
        CARD1_WIDTH = 0
        #if state == 2: 
        #exposed.append(cards[0])                
        if state == 1:
            #print cards
            #print "exposed is more than one"
            if not cards[0] in exposed:
                #print "is not in exposed"
                exposed.append(cards[0])
        elif state == 2:
            #if cards[0] in exposed:
                #CARD1_WIDTH = 50
            exposed.append(cards[0])
            #if cards[0] in exposed:
                #CARD1_WIDTH = 50
#            if cards[1] in exposed:
#                CARD2_WIDTH = CARD2_WIDTH = 50
#                CARD2_WIDTH_2 = CARD_WIDTH*2
        elif state == 3:
#            for number in exposed:
#                if number in exposed in list1_numbers and list2_numbers:
#                    exposed = [122333333, 23333]
#						exposed != []


            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2
                CARD3_WIDTH_2 = CARD_WIDTH*3     
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3	
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
                
                    
            exposed = []
            exposed.append(cards[0])
            state = 1
            print "ELSE"
#            if cards[0] in exposed:
#                CARD1_WIDTH = 50
#            if cards[1] in exposed:
#                CARD2_WIDTH = CARD2_WIDTH = 50
#                CARD2_WIDTH_2 = CARD_WIDTH*2
                
            
            
        print exposed 
        
    elif (pos[0] > 50) and (pos[0] < 100):
        CARD2_WIDTH = 0
        CARD2_WIDTH_2 = 0
        if state == 1:
            if not cards[1] in exposed:
                exposed.append(cards[1])
        if state == 2:
                exposed.append(cards[1])                
        elif state == 3:
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2
                CARD3_WIDTH_2 = CARD_WIDTH*3     
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3	
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
                
                
            exposed = []
            exposed.append(cards[1])
            state = 1
            print "ELSE"
        
        print exposed 
     
    elif (pos[0] > 100) and (pos[0] < 150):
        CARD3_WIDTH = 0
        CARD3_WIDTH_2 = 0
        if state == 1:
            if not cards[2] in exposed:
                exposed.append(cards[2])
        if state == 2:
                exposed.append(cards[2])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3	
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16            
            
            
            exposed = []
            exposed.append(cards[2])
            state = 1
            print "ELSE"      
   
            
        print exposed
        
    elif (pos[0] > 150) and (pos[0] < 200):
        CARD4_WIDTH = 0
        CARD4_WIDTH_2 = 0
        if state == 1:
            if not cards[3] in exposed:
                exposed.append(cards[3])
        if state == 2:
                exposed.append(cards[3])                
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16             
            
            
            exposed = []
            exposed.append(cards[3])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 200) and (pos[0] < 250):
        CARD5_WIDTH = 0
        CARD5_WIDTH_2 = 0
        if state == 1:
            if not cards[4] in exposed:
                exposed.append(cards[4])
        if state == 2:
                exposed.append(cards[4])                
        elif state > 2:
            
                       
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[4])
            state = 1
            print "ELSE"
            
        print exposed
       
    elif (pos[0] > 250) and (pos[0] < 300):
        CARD6_WIDTH = 0
        CARD6_WIDTH_2 = 0
        if state == 1:
            if not cards[5] in exposed:
                exposed.append(cards[5])
        if state == 2:
                exposed.append(cards[5])                
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16            
            
            
            exposed = []
            exposed.append(cards[5])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 300) and (pos[0] < 350):
        CARD7_WIDTH = 0
        CARD7_WIDTH_2 = 0
        if state == 1:
            if not cards[6] in exposed:
                exposed.append(cards[6])
        if state == 2:
                exposed.append(cards[6])                
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16               
            
            
            exposed = []
            exposed.append(cards[6])
            state = 1
            print "ELSE"

            
        print exposed
     
    elif (pos[0] > 350) and (pos[0] < 400):
        CARD8_WIDTH = 0
        CARD8_WIDTH_2 = 0
        if state == 1:
            if not cards[7] in exposed:
                exposed.append(cards[7])
        if state == 2:
                exposed.append(cards[7])                
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[7])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 400) and (pos[0] < 450):
        CARD9_WIDTH = 0
        CARD9_WIDTH_2 = 0
        if state == 1:
            if not cards[8] in exposed:
                exposed.append(cards[8])
        if state == 2:
                exposed.append(cards[8])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*6
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[8])
            state = 1
            print "ELSE"
            
            
        print exposed
        
    elif (pos[0] > 450) and (pos[0] < 500):
        CARD10_WIDTH = 0
        CARD10_WIDTH_2 = 0
        if state == 1:
            if not cards[9] in exposed:
                exposed.append(cards[9])
        if state == 2:
                exposed.append(cards[9])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[9])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 500) and (pos[0] < 550):
        CARD11_WIDTH = 0
        CARD11_WIDTH_2 = 0
        if state == 1:
            if not cards[10] in exposed:
                exposed.append(cards[10])
        if state == 2:
                exposed.append(cards[10])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16            
            
            
            exposed = []
            exposed.append(cards[10])
            state = 1
            print "ELSE"
           
            
        print exposed
        
    elif (pos[0] > 550) and (pos[0] < 600):
        CARD12_WIDTH = 0
        CARD12_WIDTH_2 = 0
        if state == 1:
            if not cards[11] in exposed:
                exposed.append(cards[11])
        if state == 2:
                exposed.append(cards[11])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[11])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 600) and (pos[0] < 650):
        CARD13_WIDTH = 0
        CARD13_WIDTH_2 = 0
        if state == 1:
            if not cards[12] in exposed:
                exposed.append(cards[12])
        if state == 2:
                exposed.append(cards[12])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[12])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 650) and (pos[0] < 700):
        CARD14_WIDTH = 0
        CARD14_WIDTH_2 = 0
        if state == 1:
            if not cards[13] in exposed:
                exposed.append(cards[13])
        if state == 2:
                exposed.append(cards[13])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[13])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 700) and (pos[0] < 750):
        CARD15_WIDTH = 0
        CARD15_WIDTH_2 = 0
        if state == 1:
            if not cards[14] in exposed:
                exposed.append(cards[14])
        if state == 2:
                exposed.append(cards[14])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[15] in exposed:
                CARD16_WIDTH = CARD_WIDTH*15
                CARD16_WIDTH_2 = CARD_WIDTH*16
            
            
            exposed = []
            exposed.append(cards[14])
            state = 1
            print "ELSE"
            
        print exposed
        
    elif (pos[0] > 750) and (pos[0] < 800):
        CARD16_WIDTH = 0
        CARD16_WIDTH_2 = 0
        if state == 1:
            if not cards[15] in exposed:
                exposed.append(cards[15])
        if state == 2:
                exposed.append(cards[15])
        elif state > 2:
            
            
            if cards[0] in exposed:
                CARD1_WIDTH = 50
            if cards[1] in exposed:
                CARD2_WIDTH = 50
                CARD2_WIDTH_2 = CARD_WIDTH*2     
            if cards[2] in exposed:
                CARD3_WIDTH = CARD_WIDTH*2	
                CARD3_WIDTH_2 = CARD_WIDTH*3
            if cards[3] in exposed:
                CARD4_WIDTH = CARD_WIDTH*3
                CARD4_WIDTH_2 = CARD_WIDTH*4
            if cards[4] in exposed:
                CARD5_WIDTH = CARD_WIDTH*4
                CARD5_WIDTH_2 = CARD_WIDTH*5
            if cards[5] in exposed:
                CARD6_WIDTH = CARD_WIDTH*5
                CARD6_WIDTH_2 = CARD_WIDTH*6
            if cards[6] in exposed:
                CARD7_WIDTH = CARD_WIDTH*6
                CARD7_WIDTH_2 = CARD_WIDTH*7
            if cards[7] in exposed:
                CARD8_WIDTH = CARD_WIDTH*7
                CARD8_WIDTH_2 = CARD_WIDTH*8
            if cards[8] in exposed:
                CARD9_WIDTH = CARD_WIDTH*8
                CARD9_WIDTH_2 = CARD_WIDTH*9
            if cards[9] in exposed:
                CARD10_WIDTH = CARD_WIDTH*9
                CARD10_WIDTH_2 = CARD_WIDTH*10
            if cards[10] in exposed:
                CARD11_WIDTH = CARD_WIDTH*10
                CARD11_WIDTH_2 = CARD_WIDTH*11
            if cards[11] in exposed:
                CARD12_WIDTH = CARD_WIDTH*11
                CARD12_WIDTH_2 = CARD_WIDTH*12
            if cards[12] in exposed:
                CARD13_WIDTH = CARD_WIDTH*12
                CARD13_WIDTH_2 = CARD_WIDTH*13
            if cards[13] in exposed:
                CARD14_WIDTH = CARD_WIDTH*13
                CARD14_WIDTH_2 = CARD_WIDTH*14
            if cards[14] in exposed:
                CARD15_WIDTH = CARD_WIDTH*14
                CARD15_WIDTH_2 = CARD_WIDTH*15
            
            
            exposed = []
            exposed.append(cards[15])
            state = 1
            print "ELSE"
            
        print exposed
    
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_text(str(cards[card_index]), [12 + card_pos, 65], 48, "White")
        canvas.draw_polygon([[0, 0], [CARD1_WIDTH, 0], [CARD1_WIDTH, CARD_HEIGHT], [0, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD2_WIDTH, 0], [CARD2_WIDTH_2, 0], [CARD2_WIDTH_2, CARD_HEIGHT], [CARD2_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD3_WIDTH, 0], [CARD3_WIDTH_2, 0], [CARD3_WIDTH_2, CARD_HEIGHT], [CARD3_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD4_WIDTH, 0], [CARD4_WIDTH_2, 0], [CARD4_WIDTH_2, CARD_HEIGHT], [CARD4_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD5_WIDTH, 0], [CARD5_WIDTH_2, 0], [CARD5_WIDTH_2, CARD_HEIGHT], [CARD5_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD6_WIDTH, 0], [CARD6_WIDTH_2, 0], [CARD6_WIDTH_2, CARD_HEIGHT], [CARD6_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD7_WIDTH, 0], [CARD7_WIDTH_2, 0], [CARD7_WIDTH_2, CARD_HEIGHT], [CARD7_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD8_WIDTH, 0], [CARD8_WIDTH_2, 0], [CARD8_WIDTH_2, CARD_HEIGHT], [CARD8_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD9_WIDTH, 0], [CARD9_WIDTH_2, 0], [CARD9_WIDTH_2, CARD_HEIGHT], [CARD9_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD10_WIDTH, 0], [CARD10_WIDTH_2, 0], [CARD10_WIDTH_2, CARD_HEIGHT], [CARD10_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD11_WIDTH, 0], [CARD11_WIDTH_2, 0], [CARD11_WIDTH_2, CARD_HEIGHT], [CARD11_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD12_WIDTH, 0], [CARD12_WIDTH_2, 0], [CARD12_WIDTH_2, CARD_HEIGHT], [CARD12_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD13_WIDTH, 0], [CARD13_WIDTH_2, 0], [CARD13_WIDTH_2, CARD_HEIGHT], [CARD13_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD14_WIDTH, 0], [CARD14_WIDTH_2, 0], [CARD14_WIDTH_2, CARD_HEIGHT], [CARD14_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD15_WIDTH, 0], [CARD15_WIDTH_2, 0], [CARD15_WIDTH_2, CARD_HEIGHT], [CARD15_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        canvas.draw_polygon([[CARD16_WIDTH, 0], [CARD16_WIDTH_2, 0], [CARD16_WIDTH_2, CARD_HEIGHT], [CARD16_WIDTH, CARD_HEIGHT]], FONT_SIZE, "Red", "Green")
        
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
