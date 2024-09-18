#include <stdio.h>

int main(void)
{
    int x,n,Y; // declaration
    int result=1; // initialization for exponent purpose
    // User input
    printf("Enter x : ");
    scanf("%d",&x);
    printf("Enter n : ");
    scanf("%d",&n);

    // Conditions for different values of n
    if (n==1) {
        Y = x+1;
        printf("\nThe value of Y = %d",Y);
    }

    else if (n==2) {
        Y = 1+x/n;
        printf("\nThe value of Y = %d",Y);
    }
    else if (n==3) {
        // calculating Power for x to the power n
        for (int i=0;i<n;i++) //iteration
        {
            result*=x;
        }
        Y = 1+ result;
        printf("\nThe value of Y = %d",Y);
    }
    else {                                           // if n>3 or n<1
        Y= 1+ n*x;
        printf("\nThe value of Y = %d",Y);
    }

}
