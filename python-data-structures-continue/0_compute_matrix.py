#!/usr/bin/python3

# function computes the square value of all integers in matrix.

def compute_matrix_(matrix=[]):
  computed_matrix = []
  for row in matrix:
    squared_row = []
    for num in row:
      squared_row += [num ** 2]
    computed_matrix += [squared_row]

  return computed_matrix

if __name__=="__main__":
  matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
  ]
  print(f"Original: {matrix}")
  print(f"Modified 2nd way: {compute_matrix_(matrix)}")

#---output---
#Original: [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#Modified 2nd way: [[81, 64, 49], [36, 25, 16], [9, 4, 1]]
