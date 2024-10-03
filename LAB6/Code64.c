#include <stdio.h>

int main() {
    int a[3][3];            //declaring
    int sum;

    // User input for matrix
    printf("Enter matrix:\n");

    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {                                          // Reading matrix
            scanf("%d", &a[i][j]);
        }
    }

    // Calculating sum of each row
    for (int i = 0; i < 3; i++) 
    {
        sum = 0 ;             //initializing sum = 0 
        for (int j = 0; j < 3; j++) 
        {
            sum += a[i][j];
        }
       
        printf("Sum of row %d: %d\n", i + 1, sum);           // Print the sum 
    }

    return 0;
}
