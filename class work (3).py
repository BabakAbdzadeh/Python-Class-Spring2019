# new study
# new study
#   conditional loops:
#   While loops:

# example:
# limit = 2000
# i = 0
# sum_of_numbers = 0
# while i < limit:
#     i = i + 1
#     sum_of_numbers = sum_of_numbers + i
# print(sum_of_numbers)

# example:
# fibonacci

# seq = [1, 1]
# i = 1
# while i < 22:
#    new_member = seq[i-1] + seq[i-2]
#    new_member = seq + [new_member]
#    print(seq)
#    i = i + 1

# another way to do this:
# members = 5
# seq = [1, 1]
# i = 1
# while len(seq) < members:
#    new_member = seq[-1] + seq[-2]
#    new_member = seq + [new_member]
#    print(seq)
# example : calculating Pi with Riemann zeta
# i = 1
# var_for_cal = 1
# n = int(input("insert n"))
# while i < n:
#     i = i + 1
#     var_for_cal = var_for_cal + var_for_cal/(i ** 2)
# pi = (var_for_cal * 6) ** 0.5
# print(pi)
# example :
# addad e aval
num = 1000001
i = 2
b = 2

while num % i != 0:
    i = i + 1

print(i==num)

