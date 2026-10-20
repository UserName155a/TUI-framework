# Text based RPG-type app
import sys
import curses
from curses import wrapper

def main(window):                       #window defines the task/window
    window.clear()
    for i in range(0,11):
        window.addstr(i,0,str("Hello")) #print() but more control over where it goes
        window.refresh()                #refresh screen, not neaded if you want instantanous anyways
    window.getkey()                     #listins to keystrokes

wrapper(main)
