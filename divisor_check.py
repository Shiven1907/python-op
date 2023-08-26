print("hello ji ^_^")
number=int(input("enter a number"))
num_1=int(input("enter first number"))
num_2=int(input("enter second number"))
num_3=int(input("enter third number"))
num_4=int(input("enter fourth number"))
num_5=int(input("enter fifth number"))
input_list=[num_1,num_2,num_3,num_4,num_5]
for elements in input_list:
     if elements % number == 0:
          print("multiple of",number,"is",elements)
          continue
print("no other multiples of", number, 'found')
          