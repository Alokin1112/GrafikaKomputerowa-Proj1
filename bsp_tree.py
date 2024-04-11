import numpy as np
import random

class BSPNode:
    def __init__(self, polygons):
        self.polygons = polygons
        self.front = None
        self.back = None
        self.partition_plane_polygon = None

def build_bsp_tree(polygons):
    if not polygons:
        return None
    
    node = BSPNode(polygons)
    random_index = random.randint(0, len(polygons) - 1)
    random_index = 0
    node.partition_plane_polygon = polygons[random_index]

    front_polygons = []
    back_polygons = []

    for idx,polygon in enumerate(polygons):
        if idx == random_index:
            continue

        side = classify_polygon(polygon, node.partition_plane_polygon.get_plane())
        if side == 1:
            front_polygons.append(polygon)
        elif side == -1:
            back_polygons.append(polygon)
        else:
            front_polygons.append(polygon)
            back_polygons.append(polygon)

    node.front = build_bsp_tree(front_polygons)
    node.back = build_bsp_tree(back_polygons)
    return node


def classify_point(point, plane):
    normal, d = plane
    distance = np.dot(normal, point.get_vector()) + d
    if distance > 0:
        return 1
    elif distance < 0:
        return -1
    else:
        return 0

def classify_polygon(polygon, plane):
    return classify_point(polygon.points[0], plane)    


def traverse_bsp_tree(node, point):
    if node is None:
        return []
    result = classify_point(point, node.partition_plane_polygon.get_plane())
    if result == 1:
        return traverse_bsp_tree(node.back, point) + [node.partition_plane_polygon] +traverse_bsp_tree(node.front, point)
    elif result == -1:
        return traverse_bsp_tree(node.front, point)+ [node.partition_plane_polygon] + traverse_bsp_tree(node.back, point) 
    else:
        return traverse_bsp_tree(node.front, point) + traverse_bsp_tree(node.back, point) 
