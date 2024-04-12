import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_figure = 0
active_color = 'white'

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []


def draw_menu():
    circle_brush = [pygame.draw.rect(screen, 'white', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'black', (35, 35), 20)
    pygame.draw.circle(screen, 'white', (35, 35), 18)
    rect_brush = [pygame.draw.rect(screen, 'white', [10, 70, 50, 50]), 1]
    pygame.draw.rect(screen, 'black', [15, 70, 37, 20], 2)

    brush_list = [circle_brush, rect_brush]

    eraser = pygame.image.load("eraser.png")
    eraser_rect = eraser.get_rect(topleft=(18, 320))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser, [18, 320, 25, 25])

    blue = pygame.draw.rect(screen, (0, 0, 255), [18, 100, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [18, 130, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [18, 160, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [18, 190, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [18, 220, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [18, 250, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [18, 280, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list


def draw_painting(paints):
    for color, pos, figure in paints:
        if color == (255, 255, 255):
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        else:
            if figure == 0:
                pygame.draw.circle(screen, color, pos, 20, 2)
            elif figure == 1:
                pygame.draw.rect(screen, color,
                                 [pos[0] - 15, pos[1] - 15, 37, 20], 2)


run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    brushes, colors, rgbs = draw_menu()

    if left_click and mouse[0] > 70:
        painting.append((active_color, mouse, active_figure))
    draw_painting(painting)

    if mouse[0] > 70:
        if active_color == (255, 255, 255):
            pygame.draw.rect(screen, active_color,
                             [mouse[0] - 15, mouse[1] - 15, 37, 20])
        else:
            if active_figure == 0:
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:
                pygame.draw.rect(screen, active_color,
                                 [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

            for i in brushes:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

    pygame.display.flip()

pygame.quit()