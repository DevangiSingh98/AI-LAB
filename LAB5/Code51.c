#include <stdio.h>

int main() {
    int i, j;      //declaration

    
    for (i = 1; i <= 5; i++)          //Looping 5 rows
    {               
        
        for (j = 1; j <= 5; j++)           // Looping 5 columns in each row
        {
            // Print '1' if the column number is equal to the row number
            if (i == j) {
                printf("1");
            } else {
                printf("0");
            }
        }
        
        printf("\n");
    }

    return 0;
}
