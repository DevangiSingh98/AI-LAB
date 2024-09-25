#include<stdio.h>

int main() {
    int a[10], sum = 0;
    
    // Reading the array elements
    printf("Enter 10 integers:\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &a[i]);
        sum += a[i];           // Adding each element to sum
    }
    
    printf("The sum of the numbers is: %d\n", sum);           // Printing the sum of the elements
    
    return 0;
}
