# new study
# new study

# function
# example:
# f = lambda x, y: x * y
# print(f(10, 12))
# num = (lambda x: x**2)(10)
# print(num)

# function with def
# example:
# def f(x) :
#     res = x ** 2
#     return res
# num = 10
# print(f(num))

# google : jeffknupp writing better functions
# import tf as tf

# mirror_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# def mirror_left(mirror_list):
#     mid = len(mirror_list) // 2
#     left_side_of_list = mirror_list[:mid]
#     mirror = left_side_of_list[::-1]
#     concat_lst = left_side_of_list + mirror
#     return concat_lst
# def mirror_right(mirror_list):
#     mid = len(mirror_list) // 2
#     right_side_of_list = mirror_list[mid:]
#     mirror = right_side_of_list[::-1]
#     concat_lst = mirror + right_side_of_list
#     return concat_lst
# print(mirror_left(mirror_list))
# print(mirror_right(mirror_list))
# def is_prime(a):
#     b = 2
#     while a % b != 0:
#         b = b + 1
#     if a == b:
#         result = True
#     else :
#         result = False
#     return result
#
# print(is_prime(14))
# sort lst list from min to max:
lst = [1, 3, 5, 9, 4, 2, 7, 11, 10]

# def my_sortted_list(lst):
#     lst_sort = []
#     i = 0
#
#     while i != len(lst):
#
#         value = min(lst)
#         lst.remove(value)
#         lst_sort.append(value)
#     return lst_sort
# print(my_sortted_list(lst))

# def bubbleSort(arr):
#     n = len(arr)
#
#     # Traverse through all array elements
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i]),
