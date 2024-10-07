#include <stdio.h>

int main() {
    int rows = 4;         //declaring and initializing

    for (int i = 1; i <= rows; i++)                  //rows
    {                  
        for (int j = 1; j <= rows - i; j++) 
        {          
            printf(" ");                 //leading spaces
        }

        for (int j = 1; j <= i; j++) 
        {                  
            printf("%d", j);                     //increaing number half
        }

        for (int j = i - 1; j >= 1; j--) 
        {              
            printf("%d", j);                   //decreasing number half
        }

        printf("\n");                                    
    }
    return 0;
}
