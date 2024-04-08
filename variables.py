import numpy as np
from math import cos, sin,pi

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
D = 200
DELTA_X = 25
DELTA_Y = 25
DELTA_Z = 25
DELTA_ANGLE_IN_DEGREES =pi/12
DELTA_ZOOM =0.20

def centerize_point(point):
  new_x = point[0] + WINDOW_WIDTH/2
  new_y = WINDOW_HEIGHT/2-point[1]
  return np.array([new_x, new_y])


def get_rotation_matrix(type_of_rotation,angle):
  if(type_of_rotation=='x'):
    return np.array([[1,0,0,0],[0,cos(angle),-sin(angle),0],[0,sin(angle),cos(angle),0],[0,0,0,1]])
  elif(type_of_rotation=='y'):
    return np.array([[cos(angle),0,sin(angle),0],[0,1,0,0],[-sin(angle),0,cos(angle),0],[0,0,0,1]])
  elif(type_of_rotation=='z'):
    return np.array([[cos(angle),-sin(angle),0,0],[sin(angle),cos(angle),0,0],[0,0,1,0],[0,0,0,1]])
  else:
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
