#!/usr/bin/python3

# function is returning a new dictionary with all values multiplied by 2
# python code using dictionary dict_

def mult_values(dict_):
  new_dict = {key: val * 2 for key, val in dict_.items()}
  return new_dict



if __name__=="__main__":
  dict_print = __import__('6_dict_print').dict_print

  dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
  new_dict = mult_values(dict_)
  dict_print(new_dict)


#--output--
#NatalieGaughan-MBA:python-datastructures-continue_1 gaughan$ python3 9_mult_values.py
#Apple: 26
#Grape: 20
#Pear: 2
#Plum: 40
