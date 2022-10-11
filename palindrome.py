str1=input("Enter the String:")
l=len(str1)
p=l-1
index=0
while(index<p):
    if(str1[index]==str1[p]):
        index=index+1
        p=p-1
    else:
        print("String is not a Palindrome")
        break
else:
    print("String is a Palindrome")        