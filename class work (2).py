# new study:
# new study:
# new study:

#   -> list

# using ( [] ) for define "list"
# example :
my_list = [10, 'hello', 10.2]
# this "list" can include all types

# searching in list
# example :
# *my_list[0]
# *print(my_list[0]) #will print first member of the list
# *type(my_list[2])  #will show the type of the member of the list
# *len(my_list) #will show us the length of the list
# example
# *length_of_my_list = len(my_list) #save the length of our list in a variable


# test
# use sum and length to calculate the sum and average of a variable numbers = [1,2,3,4,5,6,7,8]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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

# for specify the left side of the lst we can do this :
# mid = len(lst) // 2
# left_side = lst[:mid]
# left_average = sum(left_side) / mid
# and go on ....


left_side_sum = sum(lst[:7])
left_side_length = len(lst[:7])
left_side_average = (left_side_sum / left_side_length)
print(left_side_average)

right_side_sum = sum(lst[7:])
right_side_length = len(lst[7:])
right_side_average = (right_side_sum / right_side_length)
print(right_side_average)

fraction_of_left_from_right = left_side_average - right_side_average
print(fraction_of_left_from_right)

# for define empty list we can do this :
# lst = []
# for define one member list we can do this :
# lst = [1]

# new study:
# new study:
# new study:

#   -> tuples

# using ( () ) for define "tuples"
# numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# whats the difference ?
# list is mutable
# tuples are immutable
# you cant use del or some syntax's for tuples or change it in code lines ( you can change it in base writing )

# for define empty tuple wi can do this :
# tpl = ()
# for define one member tuple we can use this :
# tpl = (1,)


# pythontutor.com   --> for live help


# new study:
# new study:
# new study:

#    ->  conditions
# example

# num_1 = 1
# num_2 = 10

# comparison operators : == , > , < , >= , <=

# condition_1 = num_1 > num_2
# print(condition)    it will print False
# condition_2 = num_1 == 1
# print(condition_2)  it will print True

# logical operators : and , or , not , xor and ...

# example for declaring if number 20 is between 20 and 30
# num_1 = 20
# num_1 > 20 and num <30
# or we can write : 20 < num < 30


# new study:
# new study:
# new study:
# new study:

#  -> conditional phrases
# if
# example if 10 > 5 and 35 < 36 :
#   do some stuffs
#   do some stuffs
#   do some stuffs
# else:
#   do some other stuffs
#   do some other stuffs
#   do some other stuffs
# do some stuffs  --> this line is not in our if condition

# class work
num = 59
if num % 2 == 0 :
    print("number is even")
else:
    print("number is odd")

# if we use several if's python we run all of them
# we can use elif for conditions inside of if condition and python will run until first true or falls condition



# new study:
# new study:
# new study:

#   -> input

# example :
# value = input("please enter a number: ")
# num = int(value)
# print(num * 2)

# Class work :
# write a program that show us is input number can divide by 3 or show us the left over

input_num_variable = input("please enter a number: ")
if input_num_variable % 3 == 0 :
    print("it can be divide")
elif input_num_variable % 3 == 1:
    print("the left over is 1")
else
    print("the left over is 2")

