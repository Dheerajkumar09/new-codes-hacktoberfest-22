#include <stdio.h>
void myFunc1(){
    char c1;
    scanf(" %c",&c1);
    if (c1 != 'X')
        myFunc1();
    printf("%c", c1);
    return;   
}
int main(){
    myFunc1();
    myFunc1();
    return 0;
}