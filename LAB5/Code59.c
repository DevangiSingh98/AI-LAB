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
    printf("\n");
    printf("1st array:      ");
    for( int i = 0 ; i < 10 ; i++)
    {
        printf("%d \t", a[i]);
    }
    printf("\n");
    printf("2nd array:      ");
    for( int i = 0 ; i < 10 ; i++)
    {
        printf("%d \t", b[i]);
    }

    for(int i = 0 ; i <10 ; i++)
    {
        c[i] = a[i];
        a[i] = b[i];
        b[i] = c[i];

    }
    printf("\n");
    printf("After swapping: ");
    printf("\n");
    printf("1st Array: \n");

    for(int i = 0 ; i <10 ; i++)
    {
        printf("%d \t", a[i]);
    }
    printf("\n");
    printf("2nd Array: \n");
    for(int i = 0 ; i <10 ; i++)
    {

        printf("%d \t", b[i]);
    }

}