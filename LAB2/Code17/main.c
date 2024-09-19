#include <stdio.h>
void main()
{
    //declaration
    int x,y,z;
    //user input
    printf("Enter x:");
    scanf("%d",&x);
    printf("Enter y:");
    scanf("%d",&y);
    printf("Enter z:");
    scanf("%d",&z);
    // checking max int out of three inputted integers
    if (x > y && x > z)
        printf("Biggest number is %d", x);
    if (y > x && y > z)
        printf("Biggest number is %d", y);
    if (z > x && z > y)
        printf("Biggest number is %d", z);
}

