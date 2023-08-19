number=int(input("enter a number"))
for outer in range(1,number+1):
    for inner in range(1,21):
        print(outer,"X", inner, "=" , outer*inner)
    print()