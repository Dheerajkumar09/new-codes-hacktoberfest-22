#include<stdio.h>
#include<math.h>
int main() 
{
float p,r,t,si,ci,ci1,ci2,ci3,ci4;
p = 500000;
r = 3.5;
t = 10;
si= ((p*r*t)/100);
ci= p*pow((1+r/100),t) -p;
ci1 = p*pow((1+(r/2)/100),(t*2)) -p;
ci2 = p*pow((1+(r/4)/100),(t*4)) -p;
ci3 = p*pow((1+(r/12)/100),(t*12)) -p;
ci4 = p*pow((1+(r/365)/100),(t*365)) -p;
printf("Simple interest on Rs. 500000.00 in 10 years = %f%\n",si);
printf("Interest on Rs. 500000.00 in 10 years compounded annually = %f%\n",ci);
printf("Interest on Rs. 500000.00 in 10 years compounded semi-annually = %f%\n",ci1);
printf("Interest on Rs. 500000.00 in 10 years compounded quarterly = %f%\n",ci2);
printf("Interest on Rs. 500000.00 in 10 years compounded montly = %f%\n",ci3);
printf("Interest on Rs. 500000.00 in 10 years compounded daily = %f%\n",ci4);
}