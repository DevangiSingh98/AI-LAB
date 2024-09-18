#include <stdio.h>

int main(void)
{
    int x,table=1; //declare x and its table
    //user input: number for which its table is to be printed
    printf("Please enter a number:");
    scanf("%d", &x);
    //table of x
    for (int i = 1; i <= 10; i++) {          //iteration
        table=x*i;
        printf("%d*%d=%d\n",x,i,table);
    }
    return 0;
}
