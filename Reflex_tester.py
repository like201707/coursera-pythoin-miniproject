# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1
    
# Button handler
def click():
    global first_click, total_ticks
    if first_click:
        first_click = False
        total_ticks = 0
        timer.start()

        
    else:
        first_click = True
        timer.stop()

        print "Time between click is %.2f seconds" %(total_ticks/100.0)  
    
    

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)
timer.start()
# Start timer
frame.start()
