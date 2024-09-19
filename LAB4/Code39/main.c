#include <stdio.h>

int main()
{
    float n,sum=0,fact =1;           //declaration, initialization
    //User input for number of terms
    printf("Enter the number of terms,N : ");
    scanf("%f",&n);

    for(float i=1;i<=n;i++)                 // iterating till i=n
    {
        fact*=i;
        sum=sum+i/fact;

    }
    printf("%f",sum);
    return 0;
}
