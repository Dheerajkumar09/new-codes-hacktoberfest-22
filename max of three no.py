def max(a,b,c):
    if a>b and a>c:
        print("maximum is",a)
    elif b>a and b>c:
        print("maximum is",b)
    else:
        print("maximum is",c)
a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
c=int(input("Enter 3rd no.:"))
max(a,b,c)
