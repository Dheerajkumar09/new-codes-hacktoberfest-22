#include <stdio.h>
void myFunc1(){
    char c1;
    scanf(" %c",&c1);
    if (c1 != 'X')
        myFunc1();
    printf("%c", c1);
    return;   
}
==your code==
