ch='Y'
while (ch=='Y' or ch=='y'):
    print("Enter 1 : count words:")
    print("Enter 2 : count line:")
    print("Enter 3 : count alphabets:")
    print("Enter 4 : exit:")
    opt=int(input('enter your choice:'))
    if opt==1:
        f=open("Atoms.txt","r")
        linesList=f.readlines()
        count=0
        for line in linesList:
            wordsList=line.split()
            count = count+ len(wordsList)
        print("The number of words in this file are : ",count)
        f.close()
    elif opt==2:
        c=0
        f=open("Atoms.txt" , "r")
        line=f.readline( )
        while line:
            c=c+1
            line=f.readline( )
        print('no. of lines:',c)
        f.close( )
    elif opt==3:
        F=open('Atoms.txt','r')
        c=0
        for line in F:
            words=line.split( )
            for i in words:
                for letter in i:
                    if(letter.isalpha( )):
                        c=c+1
        print('Total no. of alphabets are:',c)
    elif opt==4:
        break
    else:
        print('invalid choice')
ch=(input('want to continue?'))
