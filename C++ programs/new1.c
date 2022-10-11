#include<stdio.h>
#include<math.h>
int main()
{
    float a,b;
    printf("Enter the distance in inches: ");
    scanf("%f",&a);
    b= a*2.54;
    printf("Distance %f inches is =%f cms",a,b);
} 