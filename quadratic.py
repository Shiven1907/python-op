a = int(input("Coefficient of x sq: "))
b = int(input("coefficient of x:"))
c = int(input("constant term"))

d = (b ** 2) - 4 * a * c

root_1=(- b + (d**0.5))/(2*a)
root_2=(- b -(d**0.5))/(2*a)

if d > 0:
    print("Real and distinct roots")
    print(root_1,root_2)

if d == 0:
    print("roots are equal: ", -b / (2*a))

if d < 0:
    print("no real roots exist")
