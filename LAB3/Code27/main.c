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
    // checking if inputted num is prime num or not
    if(flag==1) {
        printf("The number is a Prime Number");
    }
    else {
        printf("The number is not a Prime Number");
    }
}
