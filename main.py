import curses 

def main():
    stdsrc = curses.initscr()
    y, x = stdsrc.getmaxyx()

    # curses.printw("Hello World")

    stdsrc.border(0)

    preview_height = min(22, y//2)
    preview = curses.newwin(preview_height, x, 0, 0)
    preview.border()
    preview.addstr(1, 1, "This is the code preview")

    # This is the terminal
    ter = curses.newwin(y - preview_height, x, preview_height, 0)
    ter.border()
    ter.addstr(1, 1, "This is the terminal")

    stdsrc.refresh()
    preview.refresh()
    ter.refresh()

    while True:
        s = ter.getstr().decode()
        if s == "quit":
            break
        ter.addstr(s)
        try:
            ter.addstr('\n')
            # window.addstr('*', color_pair(1))
        except curses.error:
            pass

        
    stdsrc.getch()
    curses.endwin()
    print("y, x, preview_height")
    print(y, x, preview_height)


if __name__ == "__main__":
    main()