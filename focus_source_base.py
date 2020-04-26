import curses 

def main():
    # set up memory and clears the screen
    stdsrc = curses.initscr()
    
    # get the screen attributes
    y, x = stdsrc.getmaxyx()

    # stdsrc.border(0)

    # This is the preview window
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



    stdsrc.getch()
    curses.endwin()
    print("y, x, preview_height")
    print(y, x, preview_height)


if __name__ == "__main__":
    main()