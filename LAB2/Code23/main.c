#include <stdio.h>

int main(void)
{
//declaration
    int base,exponent;
    long double result=1;
    //Reading base and exponent
    printf("Enter base :\n");
    scanf("%d",&base);
    printf("Enter exponent :\n");
    scanf("%d",&exponent);

    //calculating Power
    for (int i=0;i<exponent;i++) //iteration
    {
        result*=base;
    }
    //printing result
    printf("\n%d raised to the power of %d is %.LF",base,exponent,result);

    return 0;
}
