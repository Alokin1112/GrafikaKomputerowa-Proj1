import pygame
import sys
import variables as var
from point import Point, Figure
import numpy as np
from file_reader import read_figures
pygame.init()
from bsp_tree import build_bsp_tree,traverse_bsp_tree

def print_bsptree(node):
    if node is None:
        return
    print(node.partition_plane_polygon.get_plane())
    print("P")
    print_bsptree(node.front)
    print("L")
    print_bsptree(node.back)

figures = read_figures("planes.txt")
polygons =[]
for figure in figures:
    polygons.extend(figure.get_polygons())
bsp_tree = build_bsp_tree(polygons)
print_bsptree(bsp_tree)

sorted_polygons = traverse_bsp_tree(bsp_tree, Point(0, 0, 0))
print("XXX")
for x in sorted_polygons:
    print(x.get_plane())


# for polygon in sorted_polygons:
#     polygon.draw(window,var.D)

