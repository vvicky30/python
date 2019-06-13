adhoc=[1,2,3,1,4,5,66,22,2,6,0,9] #given list

greater_five=[]
lesser_two=[]     #list

for i in adhoc : 
     if i>5 :        #appending no. to list of greater_five 
        greater_five.append(i) 
     elif i<=2 :     #appending no. to list of lesser_two
        lesser_two.append(i) 

print( f"given adhoc list:{adhoc}")
print("\nList of numbers greater than 5 in the predefied list : ",greater_five)  
print("\nList of numbers less than or equal to the predefined list : ",lesser_two)
                                              #printing numbers less than equal to 2 & greater than 5
