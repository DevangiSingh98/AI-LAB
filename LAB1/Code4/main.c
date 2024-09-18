#include <stdio.h>
int main()

{
    //Declaring temperature units
    float fahrenheit,centigrade;
    // User Input
    printf("Enter fahrenheit: ");
    scanf("%f",&fahrenheit);
    //Converting Fahrenheit to centigrade
    centigrade = (fahrenheit - 32)*5/9;
    printf("centigrade = %.2f",centigrade);
}
