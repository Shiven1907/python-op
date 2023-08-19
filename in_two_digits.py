import time
number=int(input("enter a number: "))
digits=int(input("enter even number of digits: "))
initial=0
while initial != digits/2:
     two_digits=number % 100
     time.sleep(0.5)
     print(two_digits,end=" ")
     
     number = number // 100
     initial+=1
     