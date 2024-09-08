#include <stdio.h>
void main()
{
    int a; //declaration
    //user input
    printf("Please enter a number:");
    scanf("%d", &a);
    // checking if integer inputted is even or odd
    if (a%2==0)
        printf("The number is even");
    if (a%2!=0)
        printf("The number is odd");
}
