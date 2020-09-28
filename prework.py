# Question 1 from prework

# Question 2 from prework
# Print first 100 odd numbers in Python

odd_numbers = list(range(0,101,2))
print(odd_numbers)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#    def max_num_in_list(a_list):
#        .....


def max_num_in_list(a_list):
    a_list = [1, 8, 887, 39, 60, 201, 3, 74]
    print(max(a_list))
    
max_num_in_list('a_list')

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#    def is_leap_year(a_year):
#        .....


def is_leap_year1(a_year):
    if (a_year % 4) == 0:
       if (a_year % 100) == 0:
           if (a_year % 400) == 0:
               print("True")
           else:
               print("False")
       else:
           print("True")
    else:
       print("False")

is_leap_year1(2020)

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print("True")
    elif a_year % 400 == 0:
        print("True")
    else:
        print("False")

is_leap_year(2000)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

#    def is_consecutive(a_list):
#        .....

def is_consecutive(a_list):
    a_list = [1,2,3,35,5,6,7,8,9,10]
    sorted_list = sorted(a_list)
    
    range_list = list(range(min(a_list), max(a_list)+1))      # "+1" because it stops looking at this value"
    
    if sorted_list == range_list:
        print("True")
    else:
        print("False")
        
is_consecutive('a_list')

#Joel's solution:
def is_consecutive1(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)


