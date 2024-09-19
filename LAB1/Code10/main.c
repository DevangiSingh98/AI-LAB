#include <stdio.h>

int main(void)
{
    float M,P,C,E,CM; //declaring five subjects and cut off marks
    //user input
    printf("Marks in Mathematics out of 200:");
    scanf("%f",&M);
    printf("Marks in Physics out of 200:");
    scanf("%f",&P);
    printf("Marks in Chemistry out of 200:");
    scanf("%f",&C);
    printf("Marks in entrance examination out of 100:");
    scanf("%f",&E);
    //calculating cut-off marks with given formula
    CM = M/2+P/2+C/2+E;
    printf("Cut off Marks is : %.2f ",CM);

}
