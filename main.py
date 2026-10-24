# Text based RPG-type app
import sys
import curses
from curses import wrapper
import time
import random

global cursorCoord
INPUT_LINE: int = 0
top_bar_y: int = 4

coordRef = [[4,7,16,25,34,43,52,61,70,79],
            [0,6,9,12,15,18,21,24,27,30]]

cursorCoord: list = [5,5]

makeMapFrame: bool = True
makeInfoBox: bool = True

#designs

house = [
    "  _____  ",
    " /_____\\ ",
    " |_[_]_| "
]
plain = [
    "         ",
    "         ",
    "_________"
]
mountain = [
    "  ^      ",
    " / \\/\\   ",
    "/   \\ \\  "
]
tree = [
    "   /_\\   ",
    "  /___\\  ",
    "   !_!   "
]
plot = [
    "         ",
    " ... .. .",
    "========="
]

gameMap = [
    [0  , 1,      2,      3,      4,      5,      6,      7,      8,      9     ],
    ["A", "Tree", "Tree", "Tree", "Moun", "Moun", "Moun", "Moun", "Moun", "Moun"],
    ["B", "Tree", "Tree", "Tree", "Tree", "Moun", "Moun", "Moun", "Moun", "Moun"],
    ["C", "Tree", "Tree", "Tree", "Tree", "Moun", "Moun", "Moun", "Moun", "Moun"],
    ["D", "Tree", "Tree", "Tree", "Tree", "Moun", "Moun", "Moun", "Moun", "Moun"],
    ["E", "Tree", "Tree", "Tree", "Tree", "House", "Moun", "Moun", "Moun", "Moun"],
    ["F", "Tree", "Tree", "Tree", "Tree", "Tree", "Moun", "Moun", "Moun", "Moun"],
    ["G", "Tree", "Tree", "Tree", "Tree", "Tree", "Moun", "Moun", "Moun", "Moun"],
    ["H", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree"],
    ["I", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree", "Tree"]
]

def main(window):                       #window defines the task/window

    def drawTile():


    def selectionMove(Direction):
        global cursorCoord
        if (Direction == "N") & (cursorCoord[1] > 1):
            cursorCoord[1] = cursorCoord[1] - 1
        if (Direction == "S") & (cursorCoord[1] < 9):
            cursorCoord[1] = cursorCoord[1] + 1

        if (Direction == "W") & (cursorCoord[0] > 1):
            cursorCoord[0] = cursorCoord[0] - 1
        if (Direction == "E") & (cursorCoord[0] < 9):
            cursorCoord[0] = cursorCoord[0] + 1

    def cursorPlot(Mode):
        if Mode == "add":
            window.addstr(coordRef[1][cursorCoord[1]],coordRef[0][cursorCoord[0]],"*")
        if Mode == "remove":
            window.addstr(coordRef[1][cursorCoord[1]],coordRef[0][cursorCoord[0]]," ")

    class bounds:
        Upper: 4
        Lower: 32
        Left: 3
        Right: 84 #28 cubes

    window.clear()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    window.keypad(True)
    curses.use_default_colors()

    height, width = window.getmaxyx()
    curses.resize_term(35,width)

    window.addstr(0,6,str(width)+"*"+str(height))
    
    window.addstr(1,0,str("-Start-"))
    window.addstr(33,0,str("-End-"))

    if (makeMapFrame): #makes the frame of the map
        for i in range(1,10):
            window.addstr(3*i+2,0,str("███"));window.addstr(3*i+2,84,str("███"))
            window.addstr(3*i+3,1,""+chr(64+i));window.addstr(3*i+3,85,""+chr(64+i))
            window.addstr(3*i+4,0,str("███"));window.addstr(3*i+4,84,str("███"))

        for i in range(1,10):
            window.addstr(top_bar_y,-6+9*i,str("███"+" "+str(i)+" "+"███"))

        for i in range(1,10):
            window.addstr(top_bar_y+28,-6+9*i,str("███"+" "+str(i)+" "+"███"))

    if (makeInfoBox):
        for i in range(1,30):
            window.addstr(i+3,89,"||")
        window.addstr(4,93,"Info box")
        window.addstr(5,93,"Coordinates: ["+ str(cursorCoord[0])+","+str(cursorCoord[1])+"]")
        window.addstr(6,93,"Tile:"+"[Placeholder]")
        window.addstr(15,93,"Resources")
        window.addstr(16,93,"Wood:")
        window.addstr(17,93,"Stone:")
    
    while True: #key detector
        key = window.getch()

        if key == curses.KEY_DOWN:
            window.addstr(INPUT_LINE,0,str("DOWN_"))
            cursorPlot("remove")
            selectionMove("S")

        if key == curses.KEY_UP:
            window.addstr(INPUT_LINE,0,str("UP___"))
            cursorPlot("remove")
            selectionMove("N")

        if key == curses.KEY_LEFT:
            window.addstr(INPUT_LINE,0,str("LEFT_"))
            cursorPlot("remove")
            selectionMove("W")

        if key == curses.KEY_RIGHT:
            window.addstr(INPUT_LINE,0,str("RIGHT"))
            cursorPlot("remove")
            selectionMove("E")

        window.addstr(0,13,"["+str(cursorCoord[0])+","+str(cursorCoord[1])+"]")
        window.addstr(5,93,"Coordinates: ["+ str(cursorCoord[0])+","+str(cursorCoord[1])+"]")


        cursorPlot("add")

        if key == ord('d'):
            window.clear()
            curses.nocbreak()
            curses.echo()
            curses.curs_set(1)
            window.keypad(False)
            break

        time.sleep(.001)
            

wrapper(main)
