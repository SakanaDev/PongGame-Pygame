import pygame as py
import sys

# General setup
py.init()
clock = py.time.Clock()

# Setting up the main window
screen_width = 858
screen_height = 525
screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Pong Game")

# Define color
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Rectangles
ball = py.Rect(screen_width / 2 - 9, screen_height / 2 - 9, 18, 18)
player_1 = py.Rect(screen_width - 30, screen_height / 2 - 30, 10, 60)
player_2 = py.Rect(20 , screen_height / 2 - 30, 10, 60)

# Edge 
edge_1 = py.Rect(0, 0, 2, 858)
edge_2 = py.Rect(0, 0, 858, 4)
edge_3 = py.Rect(screen_width - 2, 0, 4, 858)
edge_4 = py.Rect(0, screen_height - 2, 858, 4)

# --- Main Program Loop ---
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        
    # Visuals
    screen.fill(black)
    py.draw.rect(screen, white, edge_1)
    py.draw.rect(screen, white, edge_2)
    py.draw.rect(screen, white, edge_3)
    py.draw.rect(screen, white, edge_4)
    py.draw.ellipse(screen, white, ball)
    py.draw.rect(screen, white, player_1)
    py.draw.rect(screen, white, player_2)
    py.draw.aaline(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Updating the window
    py.display.flip()
    clock.tick(60)
