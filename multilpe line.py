def write():
    f=open("abc.txt","w")
    while True:
        line=input("Enter line:")
        f.write(line)
        choice=input("Are there more line(Y/N):")
        if choice=='N' or 'n':
            break
    f.close()    
write()