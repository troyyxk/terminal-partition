import curses 

def main():
    stdsrc = curses.initscr()

    stdsrc.addstr(0,0,"Hello World")

    stdsrc.refresh()
    stdsrc.getch()

    curses.endwin()


if __name__ == "__main__":
    main()