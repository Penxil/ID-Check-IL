import pygame as pg
from IdCheck import ID


def draw_taz(screen, font, id_text):
    pg.draw.rect(screen, (255, 255, 255), (105, 72, 570, 70))
    for index in range(min(len(id_text), 8)):
        screen.blit(font.render(id_text[index], True, (0, 0, 0)), ((137 + 70 * index), 110))


def check_y(symbols, mouse_y) -> str:
    if 230 <= mouse_y <= 300:
        return symbols[0]
    elif 320 <= mouse_y <= 390:
        return symbols[1]
    elif 420 <= mouse_y <= 480:
        return symbols[2]
    elif 500 <= mouse_y <= 570:
        return symbols[3]


def determine_digit(mouse_x, mouse_y) -> str:
    if 140 <= mouse_x <= 280:
        return check_y(('1', '4', '7', 'C'), mouse_y)
    elif 320 <= mouse_x <= 470:
        return check_y(('2', '5', '8', '0'), mouse_y)
    elif 500 <= mouse_x <= 650:
        return check_y(('3', '6', '9', '<'), mouse_y)


def draw_lines(screen) -> None:
    lastPos = (115, 150)
    for placeholder in range(1, 9):
        pg.draw.line(screen, (0, 0, 0), lastPos, (lastPos[0] + 60, 150), 2)
        lastPos = (lastPos[0] + 70, 150)
    pg.display.update()


def draw_rect(screen, text, font, coordinates) -> None:
    pg.draw.rect(screen, (0, 0, 0), coordinates)
    text_coord = ((2 * coordinates[0] + 150) // 2 - 7, (2 * coordinates[1] + 70) // 2 - 19)
    screen.blit(font.render(text, True, (255, 255, 255)), text_coord)
    pg.display.update()


def main() -> None:
    pg.init()
    programIcon = pg.image.load('icon.png')
    pg.display.set_icon(programIcon)
    font_digits = pg.font.SysFont('Arial', 25)
    font_text = pg.font.SysFont('Arial', 30, bold=True)
    background_colour = (255, 255, 255)
    (width, height) = (800, 600)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('ID-Complete')
    screen.fill(background_colour)
    pg.display.flip()
    running = True

    current_id = ''

    while running:
        pg.draw.rect(screen, (255, 255, 255), (0, 28, 545, 80))
        if len(current_id) == 8:
            check_id = ID(current_id)
            check_digit = check_id.return_check_digit()
            screen.blit(font_text.render(f"Check Digit (Luhn): {check_digit}", True, (0, 0, 0)), (270, 30))
        else:
            screen.blit(font_text.render(f"Enter 8 digits", True, (0, 0, 0)), (300, 30))

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                symbol = determine_digit(mouse_x, mouse_y)

                if symbol == 'C':
                    current_id = ''
                elif symbol == '<':
                    current_id = current_id[:len(current_id) - 1]
                elif symbol is not None and len(current_id) <= 7:
                    current_id += symbol
                draw_taz(screen, font_digits, current_id)

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.unicode in '1234567890' and len(current_id) < 8:
                    current_id += event.unicode

                if event.key == pg.K_BACKSPACE and len(current_id) > 0:
                    current_id = current_id[:len(current_id) - 1]

                draw_taz(screen, font_digits, current_id)

        line = 0
        for num_pad in range(0, 9):
            if num_pad % 3 == 0:
                line += 1
            draw_rect(screen, str(num_pad + 1), font_digits, (140 + (num_pad % 3) * 180, 140 + line * 90, 150, 70))
        draw_rect(screen, '0', font_digits, (320, 500, 150, 70))
        draw_rect(screen, 'C', font_digits, (140, 500, 150, 70))
        draw_rect(screen, '<', font_digits, (500, 500, 150, 70))
        draw_lines(screen)


if __name__ == '__main__':
    main()
