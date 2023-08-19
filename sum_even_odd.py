number=int(input("enter a number: "))
sum_even=0
sum_odd=0
a=0
for a in range(1,(number*2)+1):
     if (a % 2) == 0:
          sum_even += a
     if (a % 2) == 1:
          sum_odd += a
     
print("sum of first ",number, "even numbers is:" , sum_even)
print("sum of first ",number, "odd numbers is:" , sum_odd)
     


     
          