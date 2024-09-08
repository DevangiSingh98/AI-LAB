#include <stdio.h>
int main() {
    char c; //declaring character
    //user input
    printf("Enter a character: ");
    scanf("%c", &c);
    // converting to ascii value
    int asciiValue = (int)c;
    printf("%d\n", asciiValue);
}
