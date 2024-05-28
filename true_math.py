from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        result = int(first) / int(second)
        return result
