#include <stdio.h>

int main()
{
    int num,flag=1, sum=0;       //declaring, initializing

    printf("Enter numbers: ");         //user input
    while (flag==1)          //loop until user enters negative number
    {
        scanf("%d", &num);
        if (num >= 0)                 //sum of all positive integers
        {
            sum = sum + num;
        }
        else {                      /*if negative number is input, loop will stop
                                      and print the sum of all
                                      the positive integers entered*/
            flag = 0;
            printf("Sum: %d", sum);         //printing the sum
        }
    }

}
