#python Program which performs similar operation like "CAT" shell command
choice=int(input("Enter the command number : \n 1. Cat \t2.Cat -b\t3.Cat -s\t4.Cat -E\n:")) 
#OPEN the FILE
file=open("ved.txt","r") 
#Normal Reading like cat function 
if choice==1: 
 print(file.read()) 
elif choice==2: 
 i=1 
 for lines in file:
      if lines.strip() !="":   
           print(str(i)+". " +lines.strip())
           i+=1
elif choice==3:
 for lines in file: 
     if lines.strip() !="":
         print(lines.strip())   
elif choice==4:  
  for lines in file: 
     print(lines.strip() +"$")  
else: 
 print("Enter choice from given inputs") 
file.close()
