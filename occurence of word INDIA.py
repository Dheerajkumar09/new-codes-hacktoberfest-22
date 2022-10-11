def occurence():
    f=open("INDIA.txt","r")
    c=0
    for line in f:
        c=c+line.count('India')
    print("The word India occurs ",c,"times")
    f.close()
occurence()        
