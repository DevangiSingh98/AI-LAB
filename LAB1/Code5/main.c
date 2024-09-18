#include <stdio.h>

void main()
{
    int x,y,z; //declaration
    // user input for two numbers to swap.
    printf("Enter the value of x:");
    scanf("%d",&x);
    printf("Enter the value of y:");
    scanf("%d",&y);
    printf("The values of x and y are %d and %d respectively.",x,y);
    // z is the third variable used to swap x & y
    z = x;
    x = y;
    y = z;
    printf("\nThe values of x and y after swapping are %d and %d respectively.",x,y);


}