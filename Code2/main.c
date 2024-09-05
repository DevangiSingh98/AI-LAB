#include <stdio.h>

int main(void)
{
    //Declaring Subjects, total and Percentage
    float maths,chemistry,physics,AI,english,total,percentage;
    //User input
    printf("Enter maths marks: ");
    scanf("%f",&maths);
    printf("Enter chemistry marks: ");
    scanf("%f",&chemistry);
    printf("Enter physics marks: ");
    scanf("%f",&physics);
    printf("Enter AI marks: ");
    scanf("%f",&AI);
    printf("Enter english marks: ");
    scanf("%f",&english);
    //Calculating Total marks
    total=maths+chemistry+physics+AI+english;
    printf("Total marks: %.2f\n",total);
    //Calculating Percentage
    percentage=(total/500)*100;
    printf("Percentage: %.2f\n",percentage);
}
