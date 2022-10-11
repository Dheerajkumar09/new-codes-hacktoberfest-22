#include<stdio.h>
int main()
{
  int a;
  printf("Enter How many Subject you passed\n");
  printf("Enter 1 if you passed maths\n");
  printf("Enter 2 if you passed science\n");
  printf("Enter 3 if you passed both math and science\n");
  scanf("%d",&a);
  if(a==3)
  {
    printf("Congratulations You won Rs.45");
    
  }
  else if(a==2||a==1)
  {
    printf("Congratulations You won Rs.15");
    
  }
  else
  {
    printf("Sorry You don't won anithing");
  }
  
}