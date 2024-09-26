#include<stdio.h>
int main()
{
    int a[10];
    printf("Enter Array: ");
    
    for(int i = 0 ; i <= 9 ; i++)
    {
        scanf("%d",&a[i]);
    }

    //Reverse the given array
    printf("\n");
    printf("The reverse of the given array is: ");

    for(int i = 9 ; i > 0 ; i--)
    {
        printf("%d \t", a[i]);
    }

}