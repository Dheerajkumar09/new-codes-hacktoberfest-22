#include <stdio.h>
int Search(int arr[15],int n){
    int i;
    for(i=0;i<15;i++)
    n
        if(arr[i]==n){
            return i;
        }
        else
            continue;
    }
    return -1;
}
int main()
{
    printf("DHEERAJ KUMAR MANDVI\n");
    printf("21E079\n");
    int a[15]={69,2,35,12,4,16,8,9,1,0,31,55,45,95,87};
    int unknown;
    printf("Enter the number to be searched: ");
    scanf("%d",&unknown);
    int result=Search(a,unknown);
    printf("%d",result);
    return 0;
}
