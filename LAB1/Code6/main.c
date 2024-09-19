#include <stdio.h>

int main(void)
{
    int x,y;
    // user input for two numbers to swap
    printf("Enter x:");
    scanf("%d",&x);
    printf("Enter y:");
    scanf("%d",&y);
    printf("The values of x and y are %d and %d respectively.",x,y);
    // Code to swap x and y using XOR
    x = x^y; // value of x is now x+y
    y = x^y; //value of y is now initial value of x
    x = x^y; //value of x is now initial value of y
    printf("\nAfter Swapping: x = %d, y = %d", x, y);

    return 0;

}
