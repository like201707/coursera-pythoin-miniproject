# template for "Stopwatch: The Game"

# define global variables
import simpleguitk as simplegui


time = 0
counter = 0
counter_total = 0

# define helper function format that converts time
#def conver():
    
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global D
    A = time//600
    B = (time%600)//100
    C = (time%100)//10
    D = (time%600)%10
    return "%i:%i%i.%i" %(A, B, C, D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def Start():
    timer.start()
 
def Stop():
    global counter_total, counter, D
    counter_total += 1
    if D == 0:
        counter += 1
    timer.stop()
    
def Reset():
    global time 
    time = 0
    
# define event handler for timer with 0.1 sec interval

def timer():
    global time
    time += 1
    
def count():
    return "Your score/total times %i/%i" %(counter, counter_total)
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [160,150], 40, "White")
    canvas.draw_text(count(), [100,40], 20, "White")

timer = simplegui.create_timer(100, timer)
    
# create frame

frame = simplegui.create_frame("Stop Watch", 400, 400)

frame.set_draw_handler(draw)
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)

# register event handlers


# start frame

frame.start()
# Please remember to review the grading rubric

