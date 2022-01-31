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

# --- Main Program Loop ---
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # Updating the window
    py.display.flip()
    clock.tick(60)
