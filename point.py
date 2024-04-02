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
      (s,e)=get_line_points(start,end)
      if s is not None and e is not None:
        pygame.draw.line(window, var.BLACK, s.get_projection(d), e.get_projection(d), 1)
      
  def translate(self, vector):
    for point in self.points:
      point.translate(vector)

  def rotate(self, transformation_matrix):
    for point in self.points:
      point.rotate(transformation_matrix)

  def zoom(self, factor):
    for point in self.points:
      point.zoom(factor)

def get_line_points(start,end):
  if start.z < 0 and end.z < 0:
    return (None, None)
  new_start=start
  new_end = end
  if start.z <0:
    new_start = calculate_point_for_z_equal_zero(start, end)
  if end.z < 0:
    new_end = calculate_point_for_z_equal_zero(end, start)
  return (new_start, new_end)


def calculate_point_for_z_equal_zero(start, end):
  new_x = (start.x*end.z - end.x*start.z)/(end.z-start.z)
  new_y = (start.y*end.z - end.y*start.z)/(end.z-start.z)
  return Point(new_x, new_y, 0)

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
  
  def rotate(self,transformation_matrix):
    self.set_normalized_vector(np.dot(transformation_matrix, self.get_normalized_vector()))
  
  def zoom(self,factor):
    zoom_matrix = np.array([[factor,0,0,0],[0,factor,0,0],[0,0,factor,0],[0,0,0,1]])
    self.set_normalized_vector(np.dot(zoom_matrix, self.get_normalized_vector()))