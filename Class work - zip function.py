from typing import Tuple


def zip_(a, b):
    i = 0
    zipped = []
    while i != len(a):
        zipped: object

        first_input = (a[i], b[i])
        zipped.append(first_input)
        i += 1

    return zipped


print(zip_([1, 2, 3, 4], [5, 6, 7, 8]))
