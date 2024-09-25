#include<stdio.h>

int main() {
    int a[10], count = 0, oddcount = 0;
    // User input
    printf("Enter Array:\n");

    for (int i = 0; i < 10; i++) 
    {
        scanf("%d", &a[i]);        //Reading each element
        count ++;

        
        // Counting odd numbers
        if (a[i] % 2 != 0) 
        {
            oddcount++;
        }
    }
    
    // Printing the total number of odd elements
    printf("Total Number of elements: %d\n", count);
    printf("Total number of odd elements: %d\n", oddcount);
}