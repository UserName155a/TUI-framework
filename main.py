# Text based RPG-type app
import sys
import curses
from curses import wrapper
import time

INPUT_LINE: int = 0
top_bar_y: int = 4

make_map_frame: bool = True

class bounds:
    Upper: 4
    Lower: 32
    Left: 3
    Right: 84 #28 cubes

def main(window):                       #window defines the task/window

    window.clear()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    window.keypad(True)

    height, width = window.getmaxyx()
    curses.resize_term(35,width)

    window.addstr(0,6,str(width)+"*"+str(height))
    
    window.addstr(1,0,str("-Start-"))
    window.addstr(33,0,str("-End-"))

    if (make_map_frame): #makes the frame of the map
        for i in range(1,10):
            window.addstr(3*i+2,0,str("███"));window.addstr(3*i+2,84,str("███"))
            window.addstr(3*i+3,1,""+chr(64+i));window.addstr(3*i+3,85,""+chr(64+i))
            window.addstr(3*i+4,0,str("███"));window.addstr(3*i+4,84,str("███"))

        for i in range(1,10):
            window.addstr(top_bar_y,-6+9*i,str("███"+" "+str(i)+" "+"███"))

        for i in range(1,10):
            window.addstr(top_bar_y+28,-6+9*i,str("███"+" "+str(i)+" "+"███"))
    
    while True: #key detector
        key = window.getch()

        if key == curses.KEY_DOWN:
            window.addstr(INPUT_LINE,0,str("DOWN_"))

        if key == curses.KEY_UP:
            window.addstr(INPUT_LINE,0,str("UP___"))

        if key == curses.KEY_LEFT:
            window.addstr(INPUT_LINE,0,str("LEFT_"))

        if key == curses.KEY_RIGHT:
            window.addstr(INPUT_LINE,0,str("RIGHT"))

        if key == ord('d'):
            window.clear()
            curses.nocbreak()
            curses.echo()
            curses.curs_set(1)
            window.keypad(False)
            break

        time.sleep(.001)
            

wrapper(main)
