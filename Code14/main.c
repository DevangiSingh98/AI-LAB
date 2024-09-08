#include<stdio.h>
void main()
{
    char ch; //declaration
    //user input
    printf("enter a character:");
    scanf("%c",&ch);
    // checking ascii value to determine whether inputted char is uppercase, lowercase, a number or a special char.
    if(ch >= 65 && ch <= 90)
        printf("Upper Case Letter");
    else if(ch >= 97 && ch <= 122)
        printf("Lower Case letter");
    else if(ch >= 48 && ch <= 57)
        printf("Number");
    else
        printf("Special Symbol");
}
