# Text based Metal Detector inspired game
import curses
from curses import wrapper
import time
import math
import secrets

global cursorCoord, target, log, tries
INPUT_LINE: int = 0
top_bar_y: int = 4
target: list = [secrets.randbelow(8) + 1, secrets.randbelow(8) + 1]
log = []
tries = 0

coordRef = [[4,7,16,25,34,43,52,61,70,79],
            [0,6,9,12,15,18,21,24,27,30]]

cursorCoord: list = [5,5]

makeMapFrame: bool = True
makeInfoBox: bool = True

def main(window):                       #window defines the task/window
    global target, tries

    def selectionMove(Direction):
        global cursorCoord, tries
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
            window.addstr(coordRef[1][cursorCoord[1]], coordRef[0][cursorCoord[0]], "*")
        if Mode == "remove":
            window.addstr(coordRef[1][cursorCoord[1]], coordRef[0][cursorCoord[0]], " ")

    window.clear()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    window.keypad(True)
    curses.use_default_colors()

    height, width = window.getmaxyx()
    curses.resize_term(35, width)

    window.addstr(0, 6, str(width) + "*" + str(height))
    
    window.addstr(1, 0, "-Start-")
    window.addstr(2,0, "CONTROLS: Arrow keys for movement, 'space to flag', 'd' for exit")
    window.addstr(33, 0, "-End-")

    if (makeMapFrame): #makes the frame of the map
        for i in range(1,10):
            window.addstr(3 * i + 2, 0, str("███"));
            window.addstr(3 * i + 2, 84, str("███"))
            window.addstr(3 * i + 3, 1, "" + chr(64 + i));
            window.addstr(3 * i + 3, 85, "" + chr(64 + i))
            window.addstr(3 * i + 4, 0, str("███"));
            window.addstr(3 * i + 4, 84, str("███"))

        for i in range(1,10):
            window.addstr(top_bar_y, -6 + 9 * i, str("███" + " " + str(i) + " " + "███"))

        for i in range(1,10):
            window.addstr(top_bar_y + 28, -6 + 9 * i, str("███" + " " + str(i) + " " + "███"))

        if (makeInfoBox):
            for i in range(1,30):
                window.addstr(i + 3, 89, "||")
            window.addstr(4,93, "Info box")
            window.addstr(5,93, "Coordinates: [" + str(cursorCoord[0])+ "," + str(cursorCoord[1]) + "]")
            window.addstr(6,93, "Log:")
            window.addstr(7,93, "(Max three entries)")
    
    while True: #key detector
        key = window.getch()

        if key == curses.KEY_DOWN:
            window.addstr(INPUT_LINE, 0, str("DOWN_"))
            cursorPlot("remove")
            selectionMove("S")

        if key == curses.KEY_UP:
            window.addstr(INPUT_LINE, 0, str("UP___"))
            cursorPlot("remove")
            selectionMove("N")

        if key == curses.KEY_LEFT:
            window.addstr(INPUT_LINE, 0, str("LEFT_"))
            cursorPlot("remove")
            selectionMove("W")

        if key == curses.KEY_RIGHT:
            window.addstr(INPUT_LINE, 0, str("RIGHT"))
            cursorPlot("remove")
            selectionMove("E")

        if key == ord(' '):
            window.addstr(INPUT_LINE, 0, str("SPACE"))
            if tries < 3:
                log.append([str(cursorCoord), " --> Distance from target: " + str(round(math.sqrt(abs(cursorCoord[0] - target[0]) ** 2 + abs(cursorCoord[1] - target[1]) ** 2), 3))])
                tries = tries + 1
            else:
                if str(cursorCoord) == str(target):
                    window.addstr(20, 93, "YOU WIN")
                else:
                    window.addstr(20, 93, "YOU LOSE")
                window.addstr(21, 93, "Target was at [" + str(target[0]) + "," + chr(64 + target[1]) + "]")
            
        if key == ord('f'):
            window.addstr(INPUT_LINE, 0, str("f____"))
        
        a = 1
        for i in log:
            window.addstr(7 + a, 93, str(a) + ". [" + str(log[a - 1][0][1]) + "," + chr(64 + int(log[a - 1][0][4])) + "]" + str(log[a - 1][1]))
            window.addstr(coordRef[1][int(log[a - 1][0][4])], coordRef[0][int(log[a - 1][0][1])] - 1, "l")
            window.addstr(coordRef[1][int(log[a - 1][0][4])] - 1, coordRef[0][int(log[a - 1][0][1])] - 1, "i>")
            a = a + 1

        if a == 4:
            window.addstr(11, 93, "Guess Location! (space)")

        #window.addstr(0, 13, str(cursorCoord))
        #window.addstr(0, 19, " " + str(target))
        window.addstr(5, 93, "Coordinates: [" + str(cursorCoord[0]) + "," + str(cursorCoord[1]) + "]")

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
