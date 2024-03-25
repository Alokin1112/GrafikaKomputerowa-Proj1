from point import Point,Figure


def read_figures(file_name):
  figures=[]
  with open(file_name) as f:
    for line in f:
      points_array = []
      points_list = line.split('; ')
      for points in points_list:
        x,y,z = points.split(', ')
        points_array.append(Point(float(x),float(y),float(z)))
      figures.append(Figure(points_array))
  return figures

