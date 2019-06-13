#program to search a key entered by user by keyboard input 

import webbrowser,time 
from googlesearch import search  #importing search module from googlesearch

links=[]#list where url stored 
key = input("Enter what you want to search google : ") #here we take input search from user


for i in search(key,stop=10):  #this for loop searches top 10 url results and append them to the list 0f links
   print(i) 
   time.sleep(1)
   links.append(i)

f=open("results_url.txt","a+")  #here we save the whole links-list in file
for i in links : 
    f.write(i+"\n") 
f.close()
