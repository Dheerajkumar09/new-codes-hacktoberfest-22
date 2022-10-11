def counter():
    f= open("Sample.txt","r")
    count_to=0
    count_the=0
    for line in f:
        count_the += line.count('the')
        count_to += line.count('to')
    print("to is present",count_to,"times")
    print("the is present",count_the,"times")
    f.close()
counter()    
