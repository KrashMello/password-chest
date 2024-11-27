import sys, os
import curses
from curses import wrapper
from component.ui import card, input


def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while k != ord("q"):
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height - 1, cursor_y)

        # Declaration of strings
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(
            cursor_x, cursor_y
        )
        # Centering calculations
        start_y = int((height // 2) - 2)
        start_x_input = int((width // 2) - (40 // 2) - 40 % 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height - 1, 0, statusbarstr)
        stdscr.addstr(
            height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1)
        )
        stdscr.attroff(curses.color_pair(3))

        card(stdscr, start_x_input - 10, start_y - 10, 50, 50)
        username = input(
            stdscr,
            start_x_input,
            start_y,
            1,
            30,
            "Username: ",
        )

        password = input(
            stdscr,
            start_x_input,
            start_y + 5,
            1,
            30,
            "Password: ",
        )

        if username:
            username.edit()
            usernameMessage = username.gather()
            stdscr.addstr(
                start_y + 4, start_x_input, usernameMessage, curses.color_pair(2)
            )
        if password:
            password.edit()
            passwordMessage = password.gather()
            stdscr.addstr(
                start_y + 9, start_x_input, passwordMessage, curses.color_pair(2)
            )
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main():
    wrapper(draw_menu)


if __name__ == "__main__":
    main()
