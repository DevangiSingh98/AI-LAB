#include <stdio.h>

int main(void)
{
    int a,b,c,big; //declaration
    //user input
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    printf("Enter third number: ");
    scanf("%d", &c);
    // checking the biggest number using (?:) conditional statement
    big = (a>b&&a>c?a:b>c?b:c);
    printf("The biggest number is: %d", big);
    return 0;
}