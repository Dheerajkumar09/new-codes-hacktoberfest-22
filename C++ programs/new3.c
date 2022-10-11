#include<stdio.h>
void main()
{
int x,y,A,B;
float Result;
printf("Enter the values of x,y\n");
scanf("%d %d " ,&x, &y);
A=(x+y);
B=(x-y);
Result=A/B ;
printf("%f", Result);
}