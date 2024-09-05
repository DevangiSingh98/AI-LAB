#include <stdio.h>

int main(void)
{
    //Declaring factors of area of triangle
    float base,height,area;
    //user input
    printf("Enter the base of the triangle:");
    scanf("%f",&base);
    printf("Enter the height of the triangle:");
    scanf("%f",&height);
    //calculating area
    area=0.5*base*height;
    printf("Area of the triangle is: %.2f",area);
}
