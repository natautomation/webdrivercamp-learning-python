#!/usr/bin/python3

#function sum all unique integers in a list, one per each not takes dublicates.

def only_unique(list_=[]):
  new_set = set(list_)
  total_ = 0

  for num in new_set:
    total_ += num

  print(new_set)
  return total_
  
if __name__=="__main__":
  list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
  result = only_unique(list_)
  print(f"Sum of unique: {result}")

#--output--
#{0, 1, 2, 3, 4, 5, 6}
#Sum of unique: 21
