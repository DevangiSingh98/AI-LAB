#include <stdio.h>
int main(void)
{
    int a; //declaration
    int fact = 1; //initialization
    printf("Enter a number:");
    scanf("%d", &a);

    // iteration till i = a
    for (int i = 1; i <= a; ++i)
    {
        fact*=i; // calculating factorial of entered integer
    }
    printf("The factorial of %d is %d", a, fact);

    return 0;
}
