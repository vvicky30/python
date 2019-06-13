#! /usr/bin/python3
import datetime
y=datetime.datetime.now()  
try :
      n=input("Enter your Name : ")
      a=int(input("Enter your age : "))
      if a>250 :
          print("Error: Maximum age limit exceeded. choose age between 0-250")

      elif a<0 : 
          print("Error: Age can not be negative.") 

      elif a<95 : 
          print(f"{n} you will be 95 year old till : {((95-a)+y.year)}")

      elif a>95 : 
          print(f"{n} you became 95 year old in : {((95-a)+y.year)}")

      else :
          print(f"{n} you are 95 year old in this : {((95-a)+y.year)}")

except ValueError as e: 
     print("Error : Invalid Age format entered! plz enter right age format \n",e)
