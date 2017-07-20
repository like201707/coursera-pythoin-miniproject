# implementation of card game - Memory

import simplegui
import random

# define new game

def new_game():
    global card_on, list3, index, exposed, set_text
    card_on = 0
    set_text = 0
    list1 = [ i for i in range(0, 8)]
    list2 = list(list1)
    list3 = list1 + list2 
    random.shuffle(list3)
    exposed = []
    index0 = 0
    index1 = 0
    label.set_text("Turns = " + str(set_text))
    for i in range(16):
        exposed.append(False)
    pass


# define event handlers

def mouseclick(pos):
    global card_on, index0, index1, set_text
    if card_on == 0:
        exposed[pos[0]//50] = True
        card_on = 1
        index0 = pos[0]//50
    
    elif card_on == 1 and not exposed[pos[0]//50]:
        exposed[pos[0]//50] = True 
        card_on = 2
        index1 = pos[0]//50
        set_text += 1
    
    elif card_on == 1 and exposed[pos[0]//50]:
        pass

    else:
        if (list3[index0] != list3[index1] and 
            exposed[pos[0]//50] != exposed[index1]) :
            exposed[index0] = False
            exposed[index1] = False
            exposed[pos[0]//50] = True
            index0 = pos[0]//50        
            card_on = 1
        elif exposed[pos[0]//50] == exposed[index1]:
            pass
        else:
            exposed[pos[0]//50] = True
            index0 = pos[0]//50        
            card_on = 1
    label.set_text("Turns = " + str(set_text))
    pass            


# cards are logically 50x100 pixels in size
def draw(canvas):
    i = 0
    for num in list3:
        canvas.draw_text(str(num), (25+i*50, 50), 30, "Red")        
        i += 1
    j = 0
    for b in exposed:
        if not b:
            canvas.draw_polygon([[0+j*50, 0], [50+j*50, 0],
                             [50+j*50, 100], [0+j*50, 100]], 
                            1, "Black", "Green")
        j += 1
    pass        

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


