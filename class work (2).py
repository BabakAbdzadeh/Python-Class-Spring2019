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
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
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
# numbers variable locations start at zero (0) : numbers[0:7]
sub_numbers = numbers[:5]    # this variable contains 1 , 2, 3, 4, 5
sub_numbers2 = numbers[3:]   # this variable contains 4,5,6,7,8
# numbers[3:] is equal to numbers[3:9] or numbers[3:10] because it ends at 7
sub_numbers3 = numbers[3:7]  # this variable contains 4,5,6,7



#  -> tuples


# numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
# whats the difference ?
# list is mutable
# tuples are immutable
# you cant use del or some syntax's for tuples or change it in code lines ( you can change it in base writing )



