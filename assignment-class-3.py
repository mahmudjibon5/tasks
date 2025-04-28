#
# # Assignment 1. Find the Largest of Two Numbers
# num1 = 50
# num2 = 100
#
# if num1 > num2:
#     print( str( num1 ) + " is greater than " + str(num2) )
# else:
#     print( str(num2) + " greater than " + str(num1) )
#
#
# Assignment-2. Print Numbers from 1 to N
# _number = int( input( "Enter your desire number: " ) )
# print( type(_number) )
# for i in range(_number):
#     print( i )
#
# # Assignment 3. Check if a Number is Positive or Negative
# ass_number = int( input( "Enter your desire number: " ) )
# if ass_number > 0:
#     print( "You entered a positive number." )
# else:
#     print( "You entered a negative number" )
#
#
# 5. Find Factorial of a Number
# n = int(input("Enter a number: "))
# ini_val = 1
# for i in range(1, n + 1):
#     ini_val = ini_val * i
#
# print( n,"! =", ini_val )
#
# 6. Count Occurrences of a Digit
# input_num = input("Enter a number: ")
# src_num = input("Which digit do you want to count: ")
# count_num = input_num.count(src_num)
# print( "The digit", src_num, "appears", count_num, "time(s) in", input_num )

# 7. Find the GCD of Two Numbers

# 8. Reverse a String
# get_inp = input("Enter something: ")
# rev = ''.join( reversed(get_inp) )
# print(rev)



# 9. Check Armstrong Number


# 10. Generate a Pattern
n = int(input("Enter a number to create a pyramid: "))
for i in range(1, n):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))
