# variable number<--- input from user
# sum= 0 se start
#for a in range <-- 1 se start upto nu
# run_1---> sum=0+1=1
# run_2---> sum=1+3=4
# run_3---> sum=4+5=9
# loop will run upto number*2 plus 1

num = int(input("piliz enter a number: "))
sum=0
for addition in range (1,(num*2)+1,2):
     sum = sum + addition
     print(sum)
