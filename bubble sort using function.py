def main():
    l=[42,25,34,13,54,28]
    n=len(l)
    print("Original List: ",l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print("List after sorting is: ",l)            
main()