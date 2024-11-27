from curses import newwin
from curses.textpad import Textbox, rectangle


def input(stdscr, px, py, hieght, width, label):
    max_y, max_x = stdscr.getmaxyx()
    if py >= max_y or px >= max_x:
        return None

    if len(label) > (width - 2):
        label = label[: (width - 2)]

    stdscr.addstr(py - 1, px, label)
    editwin = newwin(hieght, width, py + 1, px + 1)
    boxWidth = px + 1 + width
    boxHieght = py + 1 + hieght
    rectangle(stdscr, py, px, boxHieght, boxWidth)
    stdscr.refresh()
    return Textbox(editwin)


def card(stdscr, px, py, height, width):
    max_y, max_x = stdscr.getmaxyx()
    if py < 0 or px < 0 or py >= max_y or px >= max_x:
        return None

    boxHeight = py + height
    boxWidth = px + width

    if boxHeight > max_y or boxWidth > max_x:
        return None

    rectangle(stdscr, py, px, 100, 100)
    stdscr.refresh()
