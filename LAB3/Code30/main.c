#include <stdio.h>

int main()
{
    int num,q,reverse=0; //declaration & initialization
    //user input
    printf("Enter a number: ");
    scanf("%d", &num);

    //iterating over every digit of inputted number
    while(num!=0) {
        q=num%10;
        reverse=reverse*10+q; //reverse of number
        num=num/10;
    }
    printf("The reverse of the number is %d",reverse);
}
