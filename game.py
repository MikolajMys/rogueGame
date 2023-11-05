import curses

def draw_map(stdscr, player_x, player_y):
    stdscr.clear()

    # Rysowanie mapy
    for i in range(20):
        for j in range(80):
            if i == 0 or i == 19:
                stdscr.addch(i, j, ord("_"))
            elif j == 0 or j == 79:
                stdscr.addch(i, j, ord("|"))
            elif i == player_y and j == player_x:
                stdscr.addch(i, j, ord("@"))
            else:
                stdscr.addch(i, j, ord(" "))

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Ukrycie kursora
    stdscr.nodelay(1)  # Ustawienie trybu non-blocking na wejściu
    stdscr.clear()

    width = 80
    height = 20
    player_x = width // 2
    player_y = height // 2

    while True:
        draw_map(stdscr, player_x, player_y)
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('w') and player_y > 1:
            player_y -= 1
        elif key == ord('s') and player_y < height - 2:
            player_y += 1
        elif key == ord('a') and player_x > 1:
            player_x -= 1
        elif key == ord('d') and player_x < width - 2:
            player_x += 1

if __name__ == "__main__":
    curses.wrapper(main)
