import time

import curses


from lyrics import *

def drawBorder(screen, x, y, width, height):
    try:
        screen.addstr(y, x, "-" * (width - 2))
        screen.addstr(y + height - 1, x, "-" * (width - 2))

        for i in range(y, y + height):
            screen.addch(i, x, "|")
            screen.addch(i, x + width - 1, "|")
    except:
        pass

def drawASCIIArt(screen, x, y, ascii_art):
    lines = ascii_art.split('\n')

    # add white space at the end of lines if line is not 40 characters
    for i in range(len(lines)):
        lines[i] += ' ' * (40 - len(lines[i]))

    # Draw it on the screen
    try:
        for i in range(len(lines)):
            screen.addstr(y + i, x, lines[i])
    except:
        pass

def drawLeftPanel(screen, left_text):
    for i, l in enumerate(left_text.split('\n')):
        screen.addstr(i + 1, 2, l)

def clearLeftPanel(screen):
    height, width = screen.getmaxyx()
    try:
        for i in range(height):
            screen.addstr(i, 0, " " * (width // 2))
        screen.refresh()
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

    # flag for done or not
    done = False

    # A variable to keep track of text in the text box
    left_text = ""

    try:
        while not done:
            # Draw the main borders
            drawBorder(screen, 0, 0, width // 2 - 1, height)
            drawBorder(screen, width // 2, 0, width // 2 - 1, height // 2)
            # screen.refresh()

            # for i in range(10):
            #     screen.addstr(i, 0, "A" * 80)
            # screen.refresh()
            # clearLeftPanel(screen)

            for line in still_alive_lyrics:

                if line.ascii_art:
                    drawASCIIArt(screen, width // 2, height // 2, line.ascii_art)
                
                if line.text == '<clear>':
                    left_text = ""
                    clearLeftPanel(screen)
                    continue
                elif line.text == '<pause>':
                    time.sleep(9999)
                    continue

                # print(line.text)
                left_text += line.text + '\n'
                drawBorder(screen, 0, 0, width // 2 - 1, height)
                drawBorder(screen, width // 2, 0, width // 2 - 1, height // 2)
                # screen.addstr(1, 1, left_text)
                drawLeftPanel(screen, left_text)

                screen.refresh()
                time.sleep(line.duration)

                screen.refresh()

            time.sleep(2)
    except:
        pass
    

if __name__ == '__main__':
    curses.wrapper(main)