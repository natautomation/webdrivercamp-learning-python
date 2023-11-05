#!/usr/bin/python3

# function returns set common elements in two sets.

def common_elements(a, b):
    result_set = set()
    for i in a:
        if i in b:
            result_set.add(i)
    return result_set


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]

#--output--
#API
#Selenium
