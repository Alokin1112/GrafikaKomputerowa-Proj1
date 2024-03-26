import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
D = 200
DELTA_X = 25
DELTA_Y = 25
DELTA_Z = 25

def centerize_point(point):
  new_x = point[0] + WINDOW_WIDTH/2
  new_y = WINDOW_HEIGHT/2-point[1]
  return np.array([new_x, new_y])