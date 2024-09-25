#include <stdio.h>

int main() {
    int i, j, n; // Decalaration
    char ch;
    //User Input
    printf("Enter n: ");
    scanf("%d",&n);
    
    for(i = 1; i <= n; i++) {
        
        // Inner loop for printing characters
        for(j = 1; j <= i; j++) {
            
            // Calculate the character to print based on j
            ch = 'A' + (j - 1);
            
            // Print the character
            printf("%c", ch);
        }
        
        printf("\n");
    }

    return 0;
}