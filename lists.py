items=[]
sum_odd=0
sum_even=0
elements=int(input("enter a number"))
for loop in range(elements+1):
     things=int(input("enter the numbers for the list"))
     if things % 2 == 0:
          sum_even += things
     else:
          sum_odd += things
     
     
     items.append(things)
     
     
print ("your list is: " , items)
print("the sum of even numbers is: ",sum_even , "the sum of odd numbers is: ", sum_odd)

     
