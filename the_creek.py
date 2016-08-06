# Made By Sokasuki

import pygame
import os

RESOLUTION = (880, 640)


class Box(object):
    def __init__(self, width, height, x_cord, y_cord, colour):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.rect = pygame.Rect(x_cord, y_cord, width, height)
        self.colour = colour
        self.range_x = range(self.x_cord, self.x_cord + width)
        self.range_y = range(self.y_cord, self.y_cord + height)
        boxes.append(self)

# Initialize Pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.mixer.init()

# Set Up Display
pygame.display.set_caption("The Creek")
SCREEN = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
font = pygame.font.SysFont("none", 40)

# Colours
BACKGROUND_C = (0, 188, 212)
TITLE_C = (33, 33, 33)
BOX_C = (255, 235, 59)

# Boxes
boxes = []
upstream_box = Box(200, 40, 65, 95, BOX_C)
downstream_box = Box(200, 40, 590, 90, BOX_C)

# Text
upstream = font.render("Upstream", True, TITLE_C)
downstream = font.render("Downstream", True, TITLE_C)

pygame.mixer.music.load('intro.aif')
pygame.mixer.music.play()

running = True
while running:

    # Boxes
    boxes = []
    upstream_box = Box(200, 40, 65, 95, BOX_C)
    downstream_box = Box(200, 40, 590, 90, BOX_C)

    # Sets Framerate
    clock.tick(60)

    # Leave Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if pos[0] in upstream_box.range_x and pos[1] in upstream_box.range_y:
                pygame.mixer.music.load('end.aif')
                pygame.mixer.music.play()
            if pos[0] in downstream_box.range_x and pos[1] in downstream_box.range_y:
                pygame.mixer.music.load('end.aif')
                pygame.mixer.music.play()

    pos = pygame.mouse.get_pos()
    if pos[0] in upstream_box.range_x and pos[1] in upstream_box.range_y:
        upstream_box.colour = (238, 213, 0)
    if pos[0] in downstream_box.range_x and pos[1] in downstream_box.range_y:
        downstream_box.colour = (238, 213, 0)

    # Draw Screen
    SCREEN.fill(BACKGROUND_C)

    for box in boxes:
        pygame.draw.rect(SCREEN, box.colour, box.rect)

    SCREEN.blit(upstream, (100, 100))
    SCREEN.blit(downstream, (600, 100))

    pygame.display.flip()
