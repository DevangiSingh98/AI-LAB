#include <stdio.h>

int main() {
    int n, element;
    int a[n];

    // User input for number of elements in linear array
    printf("Enter number of elements: ");
    scanf("%d", &n);

     

    // Input array elements
    printf("Enter elements:\n");
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &a[i]);
    }

    // User input value to search for
    printf("Enter element to search: ");
    scanf("%d", &element);

    // Perform linear search
    for (int i = 0; i < n; i++) 
    {
        if (a[i] == element) 
        {
            printf("Element %d found at index %d.\n", element, i);
            return 0; 
        }
    }
}

