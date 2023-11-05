#!/usr/bin/python3

# function returns set of elements from set.
def not_common_elements(a, b):
    result_set = set()
    for i in a:
        if i not in b:
            result_set.add(i)
        else:
            b.discard(i)
    result_set.update(b)
    return result_set


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]

#---output---
#Behave
#Cucumber
#Java
#Maven
#Python
#requests
