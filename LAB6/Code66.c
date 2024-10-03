#include <stdio.h>

int main() {
    int a[3][3], b[3][3], sum[3][3];
  

    // USer input for 1st matrix
    printf("Enter 1st matrix:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            scanf("%d", &a[i][j]);
        }
    }

    // User input for 2nd matrix
    printf("\nEnter 2nd matrix:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            scanf("%d", &b[i][j]);
        }
    }

    // Adding and storing in third matrix
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            sum[i][j] = a[i][j] + b[i][j];
        }
    }

    // Printing result
    printf("\nSum of the two matrices is:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            printf("%d ", sum[i][j]);
        }
        printf("\n");
    }

    return 0;
}
