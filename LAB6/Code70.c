#include <stdio.h>

int main() {
    int n, element, count = 0;            //declaration and initialization
    

    // Input number of elements
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int a[n];

    // User Input 
    printf("Enter elements:\n");
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &a[i]);
    }

    printf("Enter the element to count occurrences of: ");
    scanf("%d", &element);

    // Counting occurence
    for (int i = 0; i < n; i++)
     {
        if (a[i] == element) {
            count++; 
        }
    }

    printf("Element %d occurs %d times in the array.\n", element, count);
    print("\n");
    return 0; 
}
