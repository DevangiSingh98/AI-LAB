#include <stdio.h>

int main() {
    int a[3][3];
    int transpose[3][3];                //declaration

    // USer input for matrix
    printf("Enter matrix:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            scanf("%d", &a[i][j]);
        }
    }

    // transposing the matrix
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            transpose[j][i] = a[i][j];
        }
    }

    // Printing transpose of  matrix
    printf("\nTranspose of the matrix is:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            printf("%d ", transpose[i][j]);
        }
        printf("\n");
    }

    return 0;
}
