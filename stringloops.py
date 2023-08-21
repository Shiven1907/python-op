word= input("enter a sentence: ")
count_vowels=0
count_consonents=0
count_num=0
count_spaces=0
count_sp=0
for things in word :
     if things == ' ':
          count_spaces += 1
     if things in '0123456789':
          count_num += 1
     if things in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
          count_consonents += 1
     if things in 'aAeEiIoOuU':
          count_vowels += 1
     if things in """!@#$%^&*()-_=+'":;>.<,/?\|`~""":
          count_sp += 1
print("spaces are: ",count_spaces)
print("numbers are: ",count_num)
print("consonents are: ",count_consonents)
print("vowels are: ", count_vowels)   
print("special characters are: ", count_sp)  