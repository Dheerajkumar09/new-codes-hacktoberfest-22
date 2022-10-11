q=[]
ch='Y'
while(ch=='Y' or ch=='y'):
    print("Enter 1 : Enqueue")
    print("Enter 2 : Dequeue")
    opt=int(input('enter ur choice:'))
    if opt==1:
        d=int(input("enter book no : "))
        q.append(d)
    elif opt==2:
        if (q==[]):
            print( "Queue empty")
        else:
            p=q.pop(0)
            print ("Deleted element:", p)
    else:
        print('invalid choice')
ch=(input('want to continue?'))
