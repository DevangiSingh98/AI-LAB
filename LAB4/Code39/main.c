#include <stdio.h>

int main()
{
    int n,sum=0;                          //declaration, initialization
    int fact =1;
    //User input for number of terms
    printf("Enter the number of terms,N : ");
    scanf("%d",&n);

    for(int i=1;i<=n;i++)                 // iterating till i=n
    {

        for (int j=1;j<=i;++j)
        {
            fact*=j;                     // finding factorial
            sum= sum + j/fact;           // adding the numbers divided by its factorial

        }
        printf("%d",sum);
    }
    return 0;
}
