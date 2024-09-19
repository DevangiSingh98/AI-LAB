#include <stdio.h>

int main(void)
{
    int seconds,hours,minutes,s; // Declare variables for seconds, hours, minutes, and seconds
    //user input for seconds and store in 'sec'
    printf("Enter time in total seconds: ");
    scanf("%d",&seconds);
    // Calculate hours, minutes, and remaining seconds
    hours = seconds/3600;
    minutes = (seconds - (3600*hours))/60;
    s = (seconds - (3600*hours)-(60*minutes));
    // Print the time in format H:M:S
    printf("Time is: %d:%d:%d", hours,minutes,s);
    return 0;
}
