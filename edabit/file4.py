# In this challenge, you have to establish if a given integer n is a Sastry number. 
# If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
import math


def is_sastry(num1):
    num2 = num1 + 1
    concatNum = int(str(num1) + str(num2))
    number = int(math.sqrt(concatNum))

    if(number ** 2 == concatNum):
         return  str(concatNum) + " is a perfect square (" + str(number) + " ** 2)"
    else:
         return  str(concatNum) +  " is not a perfect square"
    

print(
is_sastry(183))