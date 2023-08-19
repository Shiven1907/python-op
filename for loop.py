x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
sum_all=x + y + z
sum_nondup=0
if x == y:
    sum_nondup=z
if y == z:
    sum_nondup += x
    
if x == z:
    sum_nondup += y
    
if x==y==z:
    sum_nondup += 0
    
elif x!=y!=z:
    sum_nondup=sum_all
    
print(sum_all,sum_nondup)
    