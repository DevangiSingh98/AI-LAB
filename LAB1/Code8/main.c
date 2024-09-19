#include <stdio.h>
#include <unistd.h>

int main(void)
{
    //Declaring seconds,days,hours,minutes
    long seconds;
    int days,hours,minutes;
    seconds = 31558150;
    printf("The Earth takes a period of revolution of 31558150 seconds.\n");

    //converting total seconds to days
    days = seconds/86400;
    seconds%=86400; //Remaining seconds after days

    //Converting remaining seconds to hours
    hours = seconds/3600;
    seconds%=3600;// Remaining seconds after hours

    minutes = seconds/60;//Converting remaining seconds to minutes

    sleep(1);
    printf("Converting Total Seconds in Days, hours, minutes format...");

    sleep(1);

    printf("\nThe Earth takes a period of revolution of %d days, %d hours, and %d minutes.",days,hours,minutes);

}
