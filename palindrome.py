print("To check for palindrome, Enter the S.No.")
print("To check Numbers")
print("To check Strings")
n = int(input("Enter your choice: "))
if n == 1:
    num=int(input("Enter a number:"))
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")

elif n == 2:
    str1=input("Enter the String:")
    l=len(str1)
    p=l-1
    index=0
    while(index<p):
        if(str1[index]==str1[p]):
            index=index+1
            p=p-1
        else:
            print("String is not a Palindrome!")
            break
    else:
        print("String is a Palindrome!")      
else:
        print("Enter a valid option!")
