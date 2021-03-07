import curses
import time

from image import Art
from color import Color


def main(image_path: str):
    win = curses.initscr()
    curses.start_color()

    colors = []  # массив цветов изображения
    cols, rows = curses.COLS, curses.LINES
    image = Art(image_path)
    scale_unit, console_size = image.analyze_image(cols, rows)

    for y in range(console_size):
        for x in range(console_size):
            r, g,  b, _ = image.get_rgb_pixel(x, y)
            color = Color(20+len(colors), r, g, b)
            saved_color_index = colors.index(color, 0, len(colors)) if color in colors else -1
            if saved_color_index != -1:
                color = colors[saved_color_index]
            else:
                colors.append(color)
                curses.init_color(color.id, color.red, color.green, color.blue)
                curses.init_pair(color.id, color.id, curses.COLOR_BLACK)

            win.addstr(y, x, "#", curses.color_pair(color.id))
            win.refresh()
    time.sleep(10)


if __name__ == '__main__':
    main("sticker.png")
