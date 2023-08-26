word=input("enter a word piliz: ")
length=len(word)
is_palindrome=True
for loop in range(0,length):
     if word[loop] != word[(len(word)-(loop +1))]:
          print("not a cool word eh?")
          is_palindrome=False
          break
if is_palindrome:
     print("yes it is a cool thing")
else:
     print("kuch he nahi hua ji")

"""
FOR loop op #runs-
-> range is 0 to length   loop chalega 0 se lekar 
-> run #1-----
->
->
->
->

"""
          