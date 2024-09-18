#include <stdio.h>

int main()
{
    int num,q,sum=0,N;      //declaration and initialization

    //User Input
    printf("Enter a number:");
    scanf("%d",&num);
    N=num;

    while(num>0) {
        q=num%10;    //getting remainder of number
        sum=sum+(q*q*q);     //finding cube of each digit and adding them
        num/=10;
    }
    if (N==sum) {
        printf("The number is an Armstrong Number");
    }
    else {
        printf("The number is not an Armstrong Number");
    }

}
