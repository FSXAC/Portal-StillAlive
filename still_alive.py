import time

import curses
from ascii_art import *

def drawBorder(screen, x, y, width, height):
    try:
        screen.addstr(y, x, "-" * (width - 2))
        screen.addstr(y + height - 1, x, "-" * (width - 2))

        for i in range(y, y + height):
            screen.addch(i, x, "|")
            screen.addch(i, x + width - 1, "|")
    except:
        pass

def main(screen):
    # get height and width from screen
    height, width = screen.getmaxyx()

    curses.curs_set(0)

    # must be larger than 120x80, otherwise exit
    if width < 120 or height < 40:

        # throw error
        screen.addstr(0, 0, "ERROR: Screen must be at least 120x40")
        screen.refresh()
        time.sleep(2)

    drawBorder(screen, 0, 0, width // 2 - 1, height)
    drawBorder(screen, width // 2, 0, width // 2 - 1, height // 2)
    screen.refresh()
    time.sleep(5)
    

if __name__ == '__main__':
    curses.wrapper(main)