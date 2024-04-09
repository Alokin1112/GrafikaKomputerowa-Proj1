from point import Point,Figure
import random

def read_figures(file_name):
  figures=[]
  with open(file_name) as f:
    for line in f:
      line = line.replace(" ","")
      points_array = []
      points_and_edges = line.split(';')
      points_list = points_and_edges[0].split('|')
      for points in points_list:
        x,y,z = points.split(',')
        points_array.append(Point(float(x),float(y),float(z)))
      walls_array=[]
      colors_array=[]
      walls_list = points_and_edges[1].split('|')
      for wall in walls_list:
        walls_array.append([int(x) for x in wall.split(',')])
        colors_array.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
      figures.append(Figure(points_array,walls_array,colors_array))
  return figures

