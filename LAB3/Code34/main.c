#include <stdio.h>

int main()
{
    int a,b,c,i,n;            // Declaration
    // Initialization
    a=0;
    b=1;
    printf("Enter a number");
    scanf("%d",&n);
    printf(" %d ",a);
    printf(" %d ",b);


    for(i=1;i<=n;i++) {
        c = a+b;
        printf(" %d ",c);                        // Printing the series.
        a=b;          // assigning value to previous number
        b=c;
    }
    return 0;
}

