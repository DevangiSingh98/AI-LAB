#include <stdio.h>

int main() {
    int n;        //declaration
    //USer input for number of terms,N
    printf("Enter the value of N: ");
    scanf("%d", &n);

    printf("Even numbers from 1 to %d:\n", n);

    for (int i = 2; i <= n; i += 2) {
        printf("%d ", i);  // Print even numbers
    }

    printf("\n");
    return 0;
}

