#include <stdio.h>

int main()
{
    int num,flag=1, sum=0;

    printf("Enter numbers: ");
    while (flag==1)
    {
        scanf("%d", &num);
        if (num >= 0)
        {
            sum = sum + num;
        }
        else {
            flag = 0;
            printf("Sum: %d", sum);
        }
    }

}
