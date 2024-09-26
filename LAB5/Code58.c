#include<stdio.h>
int main()
{
    int a[10],b[10],c[10];

    printf("Enter 1st Array: ");

    for( int i = 0 ; i < 10 ; i++)
    {
        scanf("%d",&a[i]);
    }

    printf("Enter 2nd Array: ");

    for( int i = 0 ; i < 10 ; i++)
    {
        scanf("%d",&b[i]);
    }

    for(int i = 0 ; i < 10 ; i++)
    {
        c[i] = a[i]+b[i];
    }
    printf("Sum of the arrays = ");
    for(int i = 0 ; i < 10 ; i++)
    {
        printf("%d \t",c[i]);
    }

}