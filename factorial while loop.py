num= int(input("Enter the number for calculating factorial: "))
fact=1
i=1
while i<=num:   #this while loop will run for every value of i until it becomes equal to the given number
   
     #this updates the value of variable 'fact' by multipling it with the value of i, everytime this loop runs
    fact= fact*i
    i = i+1
print("The factorial of ",num,"=",fact)
