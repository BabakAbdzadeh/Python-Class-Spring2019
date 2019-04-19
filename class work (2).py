# list

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

