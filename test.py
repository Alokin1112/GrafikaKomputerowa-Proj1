import pygame
import sys
import colors as c
from point import Point, Figure
from file_reader import read_figures
pygame.init()

# Set up the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Square Drawing")

# Set up colors

square_size = 100
square_x = (WINDOW_WIDTH - square_size) // 2  # Center the square horizontally
square_y = (WINDOW_HEIGHT - square_size) // 2  # Center the square vertically

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the window with white color
    window.fill(c.WHITE)

    figures = read_figures("figures.txt")

    for figure in figures:
        figure.draw(window, 200)

    # Update the display
    pygame.display.update()
