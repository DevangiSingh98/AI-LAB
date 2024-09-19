#include <stdio.h>

int main(void)
{
    char c; //declaring character
    //user input
    printf("Enter a character: ");
    scanf("%c", &c);
    //chceking if user input character is upper or lowercase
    (c >= 'a' && c <= 'z') ? printf("%c is a lowercase letter.\n", c) : printf("%c is a uppercase letter.\n", c);
}
