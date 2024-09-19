#include <stdio.h>
int main() {
    int n, p = 0, q, original; // Declaration, Initialization
    //User Input
    printf("Enter an integer: ");
    scanf("%d", &n);
    original = n;

    // reversed integer is stored in reversed variable
    while (n != 0) {
        q = n % 10;
        p = p * 10 + q;
        n /= 10;
    }

    // palindrome if input number and its reverse are equal
    if (original == p)
        printf("%d is a palindrome.", original);
    else
        printf("%d is not a palindrome.", original);

    return 0;
}