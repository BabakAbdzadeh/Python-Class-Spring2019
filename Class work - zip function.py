from typing import Tuple


def zip_(a, b):
    i = 0
    zipped: Tuple = ()
    while i != len(a):
        zipped(i) =  tuple(a[i], b[i])
        i += 1

    return zipped


print(zip_([1, 2, 3, 4], [5, 6, 7, 8]))
