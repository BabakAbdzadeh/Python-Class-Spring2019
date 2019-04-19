#   -> list

# using ( [] ) for define "list"
# example :
# *mylist = [10 , 'hello' , 10.2 ]
# this "list" can include all types

# searching in list
# example :
# *mylist[0]
# *print(mylist[0]) #will print first member of the list
# *type(mylist[2])  #will show the type of the member of the list
# *len(mylist) #will show us the length of the list
# example
# *length_of_my_list = len(mylist) #save the length of our list in a variable


# test
# use sum and length to calculate the sum and average of a variable numbers = [1,2,3,4,5,6,7,8]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
sum_number = sum(numbers)
length_number = len(numbers)
average_number = sum_number / length_number

print("sum of numbers is : ", sum_number)
print("average of numbers is: ", average_number)
# MAX and MIN will show us max and min of our list
print("the maximum value of numbers is :", max(numbers))
print("the minimum value is :", min(numbers))

# for choosing a specific part of the list :
# example :
# numbers variable locations start at zero (0) : numbers[0:9] and it is numbers[-10 : -1]
sub_numbers = numbers[:5]  # this variable contains 1 , 2, 3, 4, 5
sub_numbers2 = numbers[3:]  # this variable contains 4,5,6,7,8,9,10
# numbers[3:] is equal to numbers[3:11] or numbers[3:12] because it ends at 9
sub_numbers3 = numbers[3:7]  # this variable contains 4,5,6,7

# defining steps in list
# example from 2 until -2 with 2 step
print(numbers[2:-2:2])
# from begging to end with 2 step
print(numbers[::2])
# print backward
print(numbers[::-1])

# calculate the ( Min of right side - Min of left side) & (Max of right side - Max of left side) &
# (average of the lest side - average of the right side) of the list below:
lst = [9, 23, 1, 2, 3, 4, 5, 6, 7, 8, 77, 9, 10, 11]
left_side_sum = sum(lst[:7])
left_side_length = len(lst[:7])
left_side_average = (left_side_sum/left_side_length)
print(left_side_average)

right_side_sum = sum(lst[8:])
right_side_length = len(lst[8:])
right_side_average = (right_side_sum/right_side_length)
print(right_side_average)

fraction_of_left_from_right = left_side_average-right_side_average
print(fraction_of_left_from_right)

























#   -> tuples

# using ( () ) for define "tuples"
# numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# whats the difference ?
# list is mutable
# tuples are immutable
# you cant use del or some syntax's for tuples or change it in code lines ( you can change it in base writing )
