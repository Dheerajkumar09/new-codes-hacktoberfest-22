stk=[]
ch='Y'
while(ch=='Y' or ch=='y'):
    print("Enter 1 : Push")
    print("Enter 2 : Pop")
    opt=int(input('enter ur choice:'))
    if opt==1:
        d=int(input("enter book no : "))
        stk.append(d)
    elif opt==2:
        if (stk==[]):
            print("Stack empty")
        else:
            p=stk.pop()
            print ("Deleted element:", p)
    else:
        print('invalid choice')
ch=(input('want to continue?'))