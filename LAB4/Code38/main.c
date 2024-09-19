#include <stdio.h>

int main() {
    int n;      ///declaration

    printf("Enter number of terms, N: ");        //user input for number of terms
    scanf("%d", &n);

    printf("Squares of numbers from 1 to %d:\n", n);

    for (int i = 1; i <= n; i++) {      //incerement
        printf("%d ", i * i);        //Finding the squares
    }

    printf("\n");

}