#include <stdio.h>

int main(void)
{
    float hours, minutes, seconds,Total_seconds; //Declaring hours, minutes, seconds,Total_seconds
    //User input
    printf("Enter hours: ");
    scanf("%f", &hours);
    printf("Enter minutes: ");
    scanf("%f", &minutes);
    printf("Enter seconds: ");
    scanf("%f", &seconds);
    //Calculating Total seconds
    Total_seconds = hours * 3600 + minutes * 60 + seconds;
    printf("Total seconds: %.2f\n", Total_seconds);
}
