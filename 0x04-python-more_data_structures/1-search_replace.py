#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_elem = list(map(lambda y: replace if y == search else y, my_list))
    return (new_elem)
