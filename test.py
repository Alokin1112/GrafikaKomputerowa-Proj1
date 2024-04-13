import pygame
import sys
import variables as var
from point import Point, Figure
import numpy as np
from file_reader import read_figures
pygame.init()
from bsp_tree import build_bsp_tree,traverse_bsp_tree

# Set up the window

window = pygame.display.set_mode((var.WINDOW_WIDTH, var.WINDOW_HEIGHT))
pygame.display.set_caption("Square Drawing")
# figures =read_figures("planes.txt")
# figures = read_figures("figures.txt")
figures = read_figures("two-cubes.txt")

zoom__state=1

def translate_figures(vector):
    for figure in figures:
        figure.translate(vector)
    
def rotate_figures(axis,angle):
    for figure in figures:
        figure.rotate(var.get_rotation_matrix(axis,angle))

def zoom_figures(factor):
    global zoom__state
    if factor > 0:
        zoom__state += factor
    if factor < 0:
        if zoom__state >1:
            zoom__state +=factor
        else:
            return
    for figure in figures:
        figure.zoom(zoom__state)

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
            elif event.key ==pygame.K_q:
                rotate_figures('x',var.DELTA_ANGLE_IN_DEGREES)
            elif event.key ==pygame.K_w:
                rotate_figures('x',-var.DELTA_ANGLE_IN_DEGREES)
            elif event.key ==pygame.K_a:
                rotate_figures('y',var.DELTA_ANGLE_IN_DEGREES)
            elif event.key ==pygame.K_s:
                rotate_figures('y',-var.DELTA_ANGLE_IN_DEGREES)
            elif event.key ==pygame.K_z:
                rotate_figures('z',var.DELTA_ANGLE_IN_DEGREES)
            elif event.key ==pygame.K_x:
                rotate_figures('z',-var.DELTA_ANGLE_IN_DEGREES)
            elif event.key == pygame.K_i:
                zoom_figures(var.DELTA_ZOOM)
            elif event.key == pygame.K_o:
                zoom_figures(-var.DELTA_ZOOM)

    # Fill the window with white color
    window.fill(var.WHITE)

    polygons =[]
    for figure in figures:
        polygons.extend(figure.get_polygons())
    bsp_tree = build_bsp_tree(polygons)
    sorted_polygons = traverse_bsp_tree(bsp_tree, Point(0, 0, 0))
    for polygon in sorted_polygons:
        polygon.draw(window,var.D)

    # Update the display
    pygame.display.update()
    pygame.time.Clock().tick(60)
