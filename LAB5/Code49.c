#include<stdio.h>
int main()
{
    int i,j,n;     // Declaration

    // User Input
    printf("Enter n: ");
    scanf("%d",&n);

    for(i=1;i<n;i++)
    {   
        for(j = 1; j < n ; j++)          //printing leading spaces
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++) 
        {
            printf("*");           //printing '*'
        }
        printf("\n");
            
    }
    return 0;
}