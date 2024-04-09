import numpy as np
import pygame
import variables as var

class Figure():
  points=[]
  walls =[]
  colors=[]

  def __init__(self,points,walls,colors):
    self.points = points
    self.walls =walls
    self.colors=colors

  def draw(self,window,d):
    for idx,wall in enumerate(self.walls):
      prepared_wall = [self.points[x] for x in wall]
      array_of_points=get_line_points(prepared_wall)
      if not array_of_points is None:
        projected_points = [point.get_projection(d) for point in array_of_points]
        pygame.draw.polygon(window, self.colors[idx], projected_points)
      
  def translate(self, vector):
    for point in self.points:
      point.translate(vector)

  def rotate(self, transformation_matrix):
    for point in self.points:
      point.rotate(transformation_matrix)

  def zoom(self, factor):
    for point in self.points:
      point.zoom(factor)

def get_line_points(array_of_points):
  if all(point.z < 0 for point in array_of_points):
    return None
  new_array_of_points = []
  for i in range(len(array_of_points)):
    if array_of_points[i].z < 0:
      next_point = array_of_points[(i+1)%len(array_of_points)]
      if next_point.z < 0:
        next_point = array_of_points[(i+len(array_of_points)-1)%len(array_of_points)]
        if next_point.z < 0:
          continue
      new_point_with_z_equal_zero = calculate_point_for_z_equal_zero(array_of_points[i], next_point)
      new_array_of_points.append(new_point_with_z_equal_zero)
    else:
      new_array_of_points.append(array_of_points[i])
  return new_array_of_points


def calculate_point_for_z_equal_zero(start, end):
  new_x = (start.x*end.z - end.x*start.z)/(end.z-start.z)
  new_y = (start.y*end.z - end.y*start.z)/(end.z-start.z)
  return Point(new_x, new_y, 0)

class Point():
  x = 0
  y = 0
  z = 0
  zoom_factor = 1

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
    new_x = ((self.x*d)/(self.z+d))*self.zoom_factor
    new_y = ((self.y*d)/(self.z+d))*self.zoom_factor
    return var.centerize_point(np.array([new_x, new_y]))
  
  def translate(self, vector):
    self.set_vector(self.get_vector() + vector)
  
  def rotate(self,transformation_matrix):
    self.set_normalized_vector(np.dot(transformation_matrix, self.get_normalized_vector()))
  
  def zoom(self,factor):
    self.zoom_factor = factor