#pgm for greeting you accordingly; 
import datetime 
t = datetime.datetime.now() 
clock = t.hour 
n = input("Enter your name : " ) #input your name here
if clock<12 : 
  print(f" nice to meet you,Good morning {n}") 
elif clock<16 : 
  print(f"nice to meet you,Good afternoon {n}") 
elif clock<20 : 
  print(f"nice to meet you ,Good evening {n}") 
else :
  print(f" sweet dreams ,Good night {n}")


print(f"detailed time: {t}")
