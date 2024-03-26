import pygame
import sys
import variables as var
from point import Point, Figure
import numpy as np
from file_reader import read_figures
pygame.init()

# Set up the window

window = pygame.display.set_mode((var.WINDOW_WIDTH, var.WINDOW_HEIGHT))
pygame.display.set_caption("Square Drawing")
figures = read_figures("figures.txt")
# Main loop

def translate_figures(vector):
    for figure in figures:
        figure.translate(vector)
    
    for points in figures[0].points:
        print(points.get_vector())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                translate_figures(np.array([var.DELTA_X, 0, 0]))
            elif event.key == pygame.K_RIGHT:
                translate_figures(np.array([-var.DELTA_X, 0, 0]))
            elif event.key == pygame.K_UP:
                translate_figures(np.array([0,-var.DELTA_Y, 0]))
            elif event.key == pygame.K_DOWN:
                translate_figures(np.array([0,var.DELTA_Y, 0]))
            elif event.key == pygame.K_k:
                translate_figures(np.array([0, 0, -var.DELTA_Z]))
            elif event.key == pygame.K_l:
                translate_figures(np.array([0, 0, var.DELTA_Z]))

    # Fill the window with white color
    window.fill(var.WHITE)

    for figure in figures:
        figure.draw(window, var.D)


    # Update the display
    pygame.display.update()
    pygame.time.Clock().tick(60)
