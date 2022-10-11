def DISPLAYWORDS():
    c=0
    file=open('xyz.txt','r')
    line=file.read()
    word=line.split()
    for w in word:
        if len(w)<4:
            print(w)
    file.close()
DISPLAYWORDS()