#include <stdio.h>

int main()
{
    int num,q,sum=0; // Declaration & Initialization
    //User Input
    printf("Enter a number: ");
    scanf("%d", &num);
    //Iterating over each digit of inputted number
    while (num!=0) {
        q=num%10;
        sum=sum+q;
        num=num/10;

    }
    printf("The sum is: %d",sum);
}
