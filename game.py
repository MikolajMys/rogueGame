import curses
import random

def draw_map(stdscr, player_x, player_y, items):
    stdscr.clear()

    # Rysowanie mapy
    for i in range(20):
        for j in range(0, 82, 2):
            if i == 0:
                stdscr.addch(i, j, ord("="))
            elif j == 0 or j == 80:
                stdscr.addch(i, j, ord("|"))
            elif i == 19:
                stdscr.addch(i, j, ord("="))
            elif i == player_y and j == player_x:
                stdscr.addch(i, j, ord("@"))
            else:
                is_item = False
                for item_x, item_y, item in items:
                    if item_x == j and item_y == i:
                        stdscr.addch(i, j, ord(item))
                        is_item = True
                        break
                if not is_item:
                    stdscr.addch(i, j, ord("."))

    stdscr.refresh()

def generate_items():
    items = []
    for _ in range(3):
        item_x = random.randint(4, 76)
        item_y = random.randint(4, 16)
        item_type = random.choice(['D', '!', 'O'])
        items.append((item_x, item_y, item_type))
    return items

def write_items_to_file(items):
    with open("items_locations.txt", "w") as file:
        file.write("Locations of items:\n")
        for idx, (x, y, item) in enumerate(items, start=1):
            file.write(f"Item {idx}: X={x}, Y={y}, Type={item}\n")

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.clear()

    width = 80
    height = 20
    player_x = width // 2
    player_y = height // 2

    items = generate_items()

    while True:
        draw_map(stdscr, player_x, player_y, items)
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('w') and player_y > 1:
            player_y -= 1
        elif key == ord('s') and player_y < height - 2:
            player_y += 1
        elif key == ord('a') and player_x > 2:
            player_x -= 2
        elif key == ord('d') and player_x < width - 3:
            player_x += 2

    write_items_to_file(items)

curses.wrapper(main)