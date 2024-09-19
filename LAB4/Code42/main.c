#include <stdio.h>

int main()
{
    int num,b,flag=1;            // Declaration,Initialization
    //User input
    printf("Enter a number:");
    scanf("%d",&num);

    //iterating and incrementation
    for(b=2;b<=num/2 && flag!=0;b++) {
        if(num%b==0) {
            flag=0;
        }
    }
    if (num==1)
    {
        printf("Number is Special");
    }

    // checking if inputted num is prime num or composite
    if(flag==1) {
        printf("\nThe number is a Prime Number");
    }

    else {
        printf("The number is a Composite Number");
    }
}