import math


data = open('vectorsdata.txt', 'r')
list_of_vectors = []
for line in data:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_vectors.append(line_list)

  total_x = 0
  total_y = 0


for vector in list_of_vectors:
    magnitude = float(vector[0])
    direction = float(vector[1])
    x = magnitude * (math.cos(math.radians(direction)))
    y = magnitude * (math.sin(math.radians(direction)))
    total_x += x 
    total_y += y

printf(f'{total_x} {total_y}')