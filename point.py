import numpy as np
import pygame
import variables as var

class Figure():
  points=[]
  edges=[]#list of tuples

  def __init__(self,points,edges):
    self.points = points
    self.edges = edges

  def draw(self,window,d):
    for edge in self.edges:
      start = self.points[edge[0]]
      end = self.points[edge[1]]
      pygame.draw.line(window, var.BLACK, start.get_projection(d), end.get_projection(d), 1)
      
  def translate(self, vector):
    for point in self.points:
      point.translate(vector)

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
    return var.centerize_point(np.array([new_x, new_y]))
  
  def translate(self, vector):
    self.set_vector(self.get_vector() + vector)