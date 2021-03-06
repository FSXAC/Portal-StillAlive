
import time

import curses

import threading
from playsound import playsound


from lyrics import *

def drawBorder(screen, x, y, width, height):
    try:
        screen.addstr(y, x, "-" * (width - 1))
        screen.addstr(y + height - 1, x, "-" * (width - 1))

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
    split_text = left_text.split('\n')
    for i, l in enumerate(split_text):
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
    half_width = width // 2
    half_height = height // 2

    curses.curs_set(0)

    threading.Thread(target=playsound, args=('still_alive.mp3',)).start()

    # must be larger than 120x80, otherwise exit
    if width < 90 or height < 40:

        # throw error
        screen.addstr(0, 0, "ERROR: Screen must be at least 90x40")
        screen.refresh()
        time.sleep(5)

    # flag for done or not
    done = False

    # A variable to keep track of text in the text box
    left_text = "Hello world"

    # A variable to keep track of current line index
    current_line_index = 0

    # Keep track of character index in a line
    current_char_index = 0

    # Keep track if ascii art has been drawn or not
    ascii_art_drawn = False

    # We don't need to redraw left panel text everytime, so keep track if text changed
    left_text_changed = False

    # Keep track of left panel cursor position
    left_cursor_y = 0
    left_cursor_x = 0

    # Keep track of time
    line_start_time = time.time()
    char_start_time = time.time()

    # Cache the lyric line data
    line = still_alive_lyrics[current_line_index]
    line_text = line.text
    line_len = len(line_text)
    line_duration = line.duration
    line_total_duration = line.totalDuration()
    line_char_tdelta = line_duration / line_len

    # Cache cursor data
    cursor_char = '_'
    cursor_update_time = 0.3
    cursor_start_time = time.time()


    try:
        while not done:

            # Need refresh
            need_refresh = False
            left_text_changed = False
            cursor_changed = False

            # Clear left side if line text says clear
            if line_text == '<clear>' and left_text:
                clearLeftPanel(screen)
                left_text = ""
                left_text_changed = True

            # if there is still text to display
            if current_char_index < line_len:
                # check if times up
                if time.time() - char_start_time > line_char_tdelta:
                    # add character to left text
                    left_text += line_text[current_char_index]
                    current_char_index += 1

                    # Indicate content has changed
                    left_text_changed = True

                    # update last time
                    char_start_time = time.time()

            else:
                # if time hasn't reached total duration
                if time.time() - line_start_time < line_total_duration:
                    # do nothing
                    pass
                else:
                    # if time has reached total duration
                    # move to next line if there is still lines in the lyrics
                    if current_line_index < len(still_alive_lyrics) - 1:
                        prev_line_index = current_line_index
                        current_line_index += 1
                        current_char_index = 0

                        # fetch next line data
                        line = still_alive_lyrics[current_line_index]
                        line_text = line.text
                        line_len = len(line_text)
                        line_duration = line.duration
                        line_total_duration = line.totalDuration()
                        line_char_tdelta = line_duration / line_len

                        # reset time
                        line_start_time = time.time()
                        char_start_time = time.time()

                        # reset ascii art flag
                        ascii_art_drawn = False
                    else:
                        # if there is no more lines, exit
                        done = True

            # Draw ASCII if line activates ascii (centered in its corner)
            if line.ascii_art and not ascii_art_drawn:
                drawASCIIArt(screen, max((half_width - 40) // 2, 0) + half_width, half_height - 1, line.ascii_art)
                ascii_art_drawn = True
                need_refresh = True

            if left_text_changed:
                left_text_split = left_text.split('\n')
                left_text_split_len = len(left_text_split)

                # Draw left panel text
                drawLeftPanel(screen, left_text)

                if left_text_split_len > 1:
                    last_cursor_y = left_text_split_len - 1
                    last_cursor_x = len(left_text_split[-2]) + 2
                    screen.addch(last_cursor_y, last_cursor_x, ' ')

                # Recompute cursor position
                left_cursor_y = left_text_split_len
                left_cursor_x = len(left_text_split[-1]) + 2
                cursor_changed = True

                # Draw border
                drawBorder(screen, 0, 0, half_width - 1, height)
                drawBorder(screen, half_width, 0, half_width - 1, half_height)

                # Need to redraw
                need_refresh = True

            # Update cursor state
            if time.time() - cursor_start_time > cursor_update_time:
                cursor_start_time = time.time()
                cursor_char = '_' if cursor_char == ' ' else ' '
                cursor_changed = True

            if cursor_changed:
                screen.addch(left_cursor_y, left_cursor_x, cursor_char)
                need_refresh = True

            # Refresh screen
            if need_refresh:
                screen.refresh()
    except:
        pass

    # Exit
    curses.endwin()
    

if __name__ == '__main__':
    curses.wrapper(main)
    print('Thank you for participating in this enrichment center activity!')