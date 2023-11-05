#!/usr/bin/python3

# function returns key with largest integer value.

def max_value(d):
  if d is None or not d: # d-dictionary None or empty.
    return None

  largest_val = 0
  largest_key = None

  for key, val in d.items():
    if val > largest_val:
      largest_val = val
      largest_key = key
  return largest_key

if __name__=="__main__":
  dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
  max_key = max_value(dict_)
  print(f"Max number - {max_key}")

  max_key = max_value(None)
  print(f"Max number - {max_key}")
