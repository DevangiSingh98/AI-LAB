#include <stdio.h>

int main() {
    int n;           //declaration
    //User input
    printf("Enter number of terms, N ");
    scanf("%d", &n);

    printf("Odd numbers from 1 to %d:\n", n);

    for (int i = 1; i <= n; i += 2) {
        printf("%d ", i);  // Print odd numbers
    }

    printf("\n");
}


