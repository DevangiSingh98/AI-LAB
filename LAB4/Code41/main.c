#include <stdio.h>

int main()
{
    int n,i;      //declaration
    // User input
    printf("Enter a number: ");
    scanf("%d", &n);

    // Printing factors of given number
    printf("Factors of %d are: ", n);
    for(i = 1; i <= n; i++) {
        if(n % i == 0) {
            printf("%d ", i);
        }
    }
    return 0;
}