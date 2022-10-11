#include<stdio.h>

int main()
{
int sub1,sub2,sub3,sub4,sub5;
float avg;
printf("Enter marks of 5 subjects:");
scanf("%d%d%d%d%d",&sub1, &sub2, &sub3 ,&sub4 ,&sub5);
avg=(sub1+sub2+sub3+sub4+sub5)/5;
printf("Percentage = %f",avg);
if(avg>=60)
{
   printf("\nFirst Division");
}
else if(avg>=50)
{
   if(avg <=59)
   {
      printf("\nSecond Division");
   }
}
else if(avg >=40)
{
   if(avg <=49)
   {
       printf("\nThird Division");
   }
}
else
{
    printf("\nFail");
}
}