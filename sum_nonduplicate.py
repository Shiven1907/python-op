#duplicate numbers and addtion
num_1=int(input("enter a number"))
num_2=int(input("enter a number"))
num_3=int(input("enter a number"))
sum_all=num_1+num_2+num_3
sum_nond=0
if num_1 == num_2:
     sum_nond=num_3
if num_2 == num_3:
     sum_nond=num_1
if num_1 == num_3:
     sum_nond= num_2
if num_1 == num_2 == num_3:
     sum_nond=0
if num_1 != num_2 and num_2 != num_3 and num_1 != num_3:
     sum_nond=sum_all

print("sum of all numbers is: " , sum_all , "sum of non duplicate numbers: " , sum_nond )     
