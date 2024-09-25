#include <stdio.h>

int main() {
    int a[10], negative_count = 0, poscount = 0, zerocount = 0; // declaration & initialization
    // User input
    printf("Enter Array: \n");

    for (int i = 0; i < 10; i++) 
    { 
        scanf("%d", &a[i]);

        if(a[i]<0)
        {
            negative_count++;
        }
        else if (a[i]>0)
        {
            poscount++;
        }
        else if (a[i]=0)
        {
            zerocount++;
        }
    }
    
    printf("Total positive elements : %d\n", poscount); // Print the count

    return 0;
}
