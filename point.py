import numpy as np
import pygame
import colors as c

class Figure():
  points=[]

  def __init__(self,points):
    self.points = points

  def draw(self,window,d):
    for i in range(len(self.points)):
      point = self.points[i]
      next_point = self.points[(i+1)%len(self.points)]
      pygame.draw.line(window, c.BLACK, point.get_projection(d), next_point.get_projection(d), 1)

class Point():
  x = 0
  y = 0
  z = 0

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def get_vector(self):
    return np.array([self.x, self.y, self.z])
   
  def get_normalized_vector(self):
    return np.array([self.x, self.y, self.z, 1.0])

  def set_vector(self, vector):
    self.x = vector[0]
    self.y = vector[1]
    self.z = vector[2]
  
  def set_normalized_vector(self, vector):
    self.x = vector[0]
    self.y = vector[1]
    self.z = vector[2]

  def get_projection(self, d):
    new_x = (self.x*d)/(self.z+d)
    new_y = (self.y*d)/(self.z+d)
    return np.array([new_x, new_y])
  