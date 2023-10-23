#Input as strings
number1 = input('Enter number 1')
number2 = input('Enter number 2')
number3 = input('Enter number 3')

#Convert the input strings to integers
int_number1 = int(number1)
int_number2 = int(number2)
int_number3 = int(number3)

print(int_number1,int_number2)

sum = int_number1+int_number2+int_number3
print(sum)

difference = int_number1-int_number2-int_number3
multiplication = int_number1*int_number2*int_number3
division = (int_number2/int_number1)/int_number3

print(difference,multiplication,division)

import math

print(math.pow(9,3))
print(math.ceil(1.4))
print(math.acos(-0.55))
print(math.factorial(9))
print(math.log(2))
print(math.trunc(2.77))
print(math.tanh(8))
print (math.degrees(8.90))
print (math.remainder(9, 2))
print(math.floor(1.4))
print (math.lgamma(7))