#!/usr/bin/python3
#here we make command inline function


import sys
num1=sys.argv[1]#this will print inline input
num2=sys.argv[2]
print(num1)
print(num2)


#definition of function
def add_mul(x,y):
    print("addition is:",x+y)
    print("multiplication is:",x*y)


#call
add_mul(int(num1),int(num2))
