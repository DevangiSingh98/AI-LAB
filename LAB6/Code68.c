 #include <stdio.h>

int main() {
    int a[3][3], b[3][3], product[3][3];
  

    // User input for 1st matrix
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
 
    // Initializing  product matrix = 0
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            product[i][j] = 0;
        }
    }

    // Multiplying 
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            for (int k = 0; k < 3; k++) 
            {
                product[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Printing 
    printf("\nProduct of the two matrices is:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            printf("%d ", product[i][j]);
        }
        printf("\n");
    }

    return 0;
}