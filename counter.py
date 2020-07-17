# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
counter = 15
# Reset global count to zero.
def reset():
    global counter
    counter = counter - counter
    return counter
# Increment global count.
def increment():
    global counter
    counter = counter + 1
    return counter
# Decrement global count.
def decrement():
    global counter
    counter = counter - 1
    return counter
# Print global count.print_count():
def print_count():
    print counter


    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2
