import curses
import time

def main(stdscr):
    curses.curs_set(0) 
    stdscr.nodelay(1)

    message = "Hello world"
    height, width = stdscr.getmaxyx()
    y, x = 0, width // 2 - len(message) // 2
    direction = 1

    while True:
        stdscr.clear()
        stdscr.addstr(y, x, message)
        stdscr.refresh()
        time.sleep(0.1)

        y += direction
        if y <= 0 or y >= height - 1:
            direction *= -1

if __name__ == "__main__":
    curses.wrapper(main)
