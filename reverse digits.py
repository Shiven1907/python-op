# Ek number input mein stored
# ek counter variable
# reversed digit ko initally zero stored
#while loop start(while condition(number input (froom user)is not equal to 0))
#while loop start hoga ek number aayega  
#a new variable (x) <--- mod by 10 will give a remainder of a single digit(1-9)
#the remainder variable is recalled and is multiplied by 10 on itself plus the remainder (x)
#number floor division by 10 
#the number will losse its units place and will become a digit less
import time
number= int(input("enter a number"))
reversed_digit=0
while number != 0:
     remiander=number%10
     reversed_digit = reversed_digit*10 + remiander
     number = number//10
     time.sleep(1)
     print(reversed_digit)
