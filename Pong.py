
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
vert_vel_l = - random.randrange(2, 4)
hori_vel_l = - random.randrange(2, 4)
vert_vel_r = - random.randrange(2, 4)
hori_vel_r =  random.randrange(2, 4)
paddle1_pos_x = [PAD_WIDTH, HEIGHT / 2]
paddle1_pos_y = [PAD_WIDTH, PAD_HEIGHT]
paddle1_vel = [0, 0]
paddle2_pos_x = [WIDTH - PAD_WIDTH, HEIGHT / 2]
paddle2_pos_y = [WIDTH - PAD_WIDTH, PAD_HEIGHT]
paddle2_vel = [0, 0]
paddle1_pos = [paddle1_pos_x, paddle1_pos_y]
#paddle1_pos = [HALF_PAD_WIDTH, HALF_PAD_HEIGHT]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_pos = [18, HEIGHT / 2]
    direction = random.randrange(1, 3)    
    if direction == 1:
        direction = LEFT
    elif direction == 2:
        direction = RIGHT
    if direction == LEFT:
        ball_vel = [hori_vel_l, vert_vel_l]
    elif direction == RIGHT:
        ball_vel = [hori_vel_r, vert_vel_r]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(new_game)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")   
    
    # position of paddles
    paddle1_text_pos_x = [ paddle1_pos_x[0]+4, paddle1_pos_x[1]-4]
    canvas.draw_text(str(paddle1_pos_x), paddle1_text_pos_x, 20, 'Red')
    paddle1_text_pos_y = [ paddle1_pos_y[0]+4, paddle1_pos_y[1]+14]
    canvas.draw_text(str(paddle1_pos_y), paddle1_text_pos_y, 20, 'Red')
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    ball_text_pos = [ ball_pos[0]+20, ball_pos[1]]
    canvas.draw_text(str(ball_text_pos), ball_text_pos, 20, 'Red')
    if ball_pos[0] == BALL_RADIUS+10:
        print "ball position: " + str(ball_pos)
        print "paddle pos x: " + str(paddle1_pos_x)
        print "paddle pos y: " + str(paddle1_pos_y)
        if( (ball_pos[1] > paddle1_pos_y[1]) and (ball_pos[1] < paddle1_pos_x[1]) ):
            print "ball within paddle"
        else:
            print "LOST"
        #if ball_pos[0] == 40:
        #    ball_vel[0] =- ball_vel[0]
            
        #    print ball_pos
        #elif ball_pos[0] == BALL_RADIUS:
        #    print ball_pos
        #else:
            #print ball_pos
        #    ball_pos = [WIDTH / 2, HEIGHT / 2]
        #    direction = spawn_ball(RIGHT)
    #elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        #ball_pos = [WIDTH / 2, HEIGHT / 2]
        #direction = spawn_ball(LEFT)
        #ball_vel[0] = - ball_vel[0]
        
        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos_x[1] += paddle1_vel[1]
    paddle1_pos_y[1] += paddle1_vel[1]
    
    paddle2_pos_x[1] += paddle2_vel[1]
    paddle2_pos_y[1] += paddle2_vel[1]
    
    if paddle1_pos_x[1] >= HEIGHT:
        paddle1_pos_x[1] = HEIGHT
        paddle1_pos_y[1] = (HEIGHT/2)+PAD_HEIGHT

    if paddle1_pos_y[1] <= 0:
        paddle1_pos_x[1] = (HEIGHT/2)-PAD_HEIGHT
        paddle1_pos_y[1] = 0
        
    if paddle2_pos_x[1] >= HEIGHT:
        paddle2_pos_x[1] = HEIGHT
        paddle2_pos_y[1] = (HEIGHT/2)+PAD_HEIGHT

    if paddle2_pos_y[1] <= 0:
        paddle2_pos_x[1] = (HEIGHT/2)-PAD_HEIGHT
        paddle2_pos_y[1] = 0        
        
    # draw paddles
    canvas.draw_line(paddle1_pos_x, paddle1_pos_y, PAD_WIDTH, "White")   

    canvas.draw_line(paddle2_pos_x, paddle2_pos_y, PAD_WIDTH, "White")
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel, acc
    acc = 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acc 
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel [1] += acc
def keyup(key):
    global paddle1_vel, paddle2_vel, acc
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] -= acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] -= acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
