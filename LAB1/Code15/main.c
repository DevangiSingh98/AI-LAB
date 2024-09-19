#include<stdio.h>

int main(void)
{
    float percentage,maths,IoP,english,CS,ENA,total;//Declaring five subjects,percentage and total
    // user input for marks of five subjects
    printf("Enter maths marks:\n");
    scanf("%f",&maths);
    printf("Enter IoP marks:\n ");
    scanf("%f",&IoP);
    printf("Enter english marks:\n");
    scanf("%f",&english);
    printf("Enter CS marks:\n");
    scanf("%f",&CS);
    printf("Enter ENA marks:\n");
    scanf("%f",&ENA);
    //Total marks
    total = maths + IoP + english + CS + ENA;
    //Calculating the Percentage
    percentage = (total/500)*100;
    //Checking which division the percentage falls into
    if (percentage>=60 && percentage<=100) {
        printf("First Division");
    }
    else if (percentage>=50 && percentage<=59.90) {
        printf("Second Division");
    }
    else if (percentage>=30 && percentage<=49.90) {
        printf("Third Division");
    }
    else {
        printf("Fail...");
    }
    return 0;
}
