num= int(input("Enter the number for calculating factorial: "))
fact=1
i=1
while i<=num:
    fact= fact*i
    i = i+1
print("The factorial of ",num,"=",fact)    
