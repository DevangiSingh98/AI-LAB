#include <stdio.h>
void main()
{
    //Declaring the factors of simple interest
    int p,r,t,simple_interest;
    //user input
    printf("Enter Principal Number:");
    scanf("%d",&p);
    printf("Enter Rate of Interest:");
    scanf("%d",&r);
    printf("Enter number of years:");
    scanf("%d",&t);
    //Calculating Simple Interest
    simple_interest=(p*r*t)/100;
    printf("Simple Interest is %d",simple_interest);
}