#include <stdio.h>

int main() {
    int i, j, n;

    printf("Enter n: ");
    scanf("%d",&n);

    for (i = 1; i <= n; i++) {
        // Print leading spaces
        for (j = i; j < n; j++) {
            printf(" ");
        }
        // Print numbers
        for (j = 1; j <= i; j++) {
            printf("%d", j);
        }
        // Move to the next line
        printf("\n");
    }

    return 0;
}

