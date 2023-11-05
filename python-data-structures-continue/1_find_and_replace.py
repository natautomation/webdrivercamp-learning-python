#!/usr/bin/python3

# function replace all element occurrences

def find_replace_(original, find, replace):
  new_list = []
  for num in original:
    if num == find:
      num = replace
    new_list += [num]
  return new_list

if __name__=="__main__":
  original = [0, 11, 13, 9, 4, 3, 4, 7, 7, 1, 0, 9]
  modified1 = find_replace_(original, 9, 13)

  print(f"Original : {original}")
  print(f"Modified1: {modified1}")

#Original : [0, 11, 13, 9, 4, 3, 4, 7, 7, 1, 0, 9]
#Modified1: [0, 11, 13, 13, 4, 3, 4, 7, 7, 1, 0, 13]
