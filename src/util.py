import pprint
import math
from statistics import mean
import ntpath


def path_leaf(path):
    """An OS agnostic function to extract the filename from a provided path"""
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def pretty_print(dictionary):
    pprint.pprint(dictionary)


def list_avg(l):
    return mean(l)


def count_matches(x, y):
    matching_value_count = 0
    x_keys = list(x.keys())
    x_values = list(x.values())
    y_keys = list(y.keys())
    y_values = list(y.values())
    if len(x) > len(y):
        for i in range(len(y_keys)):
            if math.isclose(list_avg(x_values[i]), list_avg(y_values[i])):
                matching_value_count += 1
            return matching_value_count
    # This case is only reached if the len(y) > len(x). We use the length of x_keys to iterate because otherwise we will
    # go outside the array bounds
    for i in range(len(x_keys)):
        if math.isclose(list_avg(x_values[i]), list_avg(y_values[i])):
            matching_value_count += 1
    return matching_value_count
