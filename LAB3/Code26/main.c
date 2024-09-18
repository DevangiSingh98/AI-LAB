#include <stdio.h>

int main(void)
{
    int even,odd,n; // declaring number(odd/even)
    int i =1; // declaring & initializing
    printf("Enter n: ");
    scanf("%d",&n);

    while(i<=n) {        // iteration
        // Calculating sum of all even numbers
        if (i%2==0)
        {
            even+=i;
        }
        // Calculating sum of all odd numbers
        else {
            odd+=i;
        }
        i+=1;
    }
    // printing the result
    printf("\nSum of all even numbers from one to %d= %d",n,even);
    printf("\nSum of all odd numbers from one to %d= %d",n,odd);
}
