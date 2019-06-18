#!/usr/bin/python3
#*args with first extra argument or we can say fixed argument
# whereas *args arguments are dependent upon calling of function with umber of arguments
def snoop(arg1, *argv):
  print("first argument:",arg1)
  for arg in argv:
   print("next argument through *argv:",arg)

snoop('vedant','bhatt','theseus','supreme','gucci')
