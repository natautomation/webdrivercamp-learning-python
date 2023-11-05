#!/usr/bin/python3

# function returns weight average.

def calc_weight(list_=[]):
  if len(list_) == 0:   #if not list_:
    return 0
  else:
    weighted_sum_num = 0  #Initialize variables
    total_weight = 0

    for i in list_:
        a, b = i
        weighted_sum_num += a * b
        total_weight += b

    return weighted_sum_num / total_weight


         # weighted average calculated dividing total multiplied values on total weights

if __name__=="__main__":
  list_ = [(3, 2), (5, 9), (7, 7)]
  # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
  result = calc_weight(list_)
  print(f"Weight: {result:0.2f}")

#-----output-----
#Weight: 5.56
