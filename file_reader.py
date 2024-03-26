from point import Point,Figure


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
      edges_array=[]
      edges_list = points_and_edges[1].split('|')
      for edge in edges_list:
        start,end = edge.split(',')
        edges_array.append((int(start),int(end)))
      figures.append(Figure(points_array,edges_array))
  return figures

