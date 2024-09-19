#include <stdio.h>

int main() {
    int n, num, max, min;

    printf("Enter the number of numbers: ");
    scanf("%d", &n);

    if (n < 1) {
        printf("At least 1 number is required!\n");
    }

    printf("Enter the numbers:\n");

    // Read the first number and initialize both max and min
    scanf("%d", &num);
    max = num;
    min = num;

    // Loop through the remaining numbers
    for (int i = 1; i < n; i++) {
        scanf("%d", &num);

        if (num > max) {             //checking for max and min
            max = num;
        }

        if (num < min) {
            min = num;
        }
    }

    printf("Maximum: %d\n", max);
    printf("Minimum: %d\n", min);

}
