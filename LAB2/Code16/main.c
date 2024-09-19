#include <stdio.h>
void main()
{
    int x,y,z;//declaration
    //user input
    printf("Enter x:");
    scanf("%d",&x);
    printf("Enter y:");
    scanf("%d",&y);
    printf("Enter z:");
    scanf("%d",&z);
    //checking if x is greater than y
    if (x > y)
    {
        if (x > z) //checking if x is greater than z
        {
            printf("The greatest number is %d",x);
        }
        else // z is greater than x
        {
            printf("The greatest number is %d",z);
        }
    }
    else // y is greater than x then...
    {
        if (y>z) // checking if y is greater than z
        {
            printf("The greatest number is %d",y);
        }
        else // z is the greatest integer
        {
            printf("The greatest number is %d",z);
        }
    }
}