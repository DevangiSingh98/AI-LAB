#include <stdio.h>
int main(void)
{
    //declaration
    char operator;
    int a,b;
    //user input: choosing the operation to be performed
    printf("Enter operator (+,-,*,/):");
    scanf("%c",&operator);
    //user input: entering operands
    printf("Enter two numbers:");
    scanf("%d%d",&a,&b);

    //checking operator entered using switch case
    switch(operator) {
        case '+':
            printf("%d + %d = %d",a,b,a+b);
            break;
        case '-':
            printf("%d + %d = %d",a,b,a+b);
            break;
        case '*':
            printf("%d * %d = %d",a,b,a*b);
            break;
        case '/':
            printf("%d / %d = %d",a,b,a/b);
            break;
        default:
            printf("Invalid operator");
    }

    return 0;
}
