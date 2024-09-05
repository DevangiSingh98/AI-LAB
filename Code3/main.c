#include <stdio.h>

int main(void)
{
    //Declaring factors of gross salary
    int basic,rent,transport,fbp,bonus,incometax,fund,gross;
    //user input
    printf("Enter Basic Salary:");
    scanf("%d",&basic);
    printf("Enter House Rent Allowance:");
    scanf("%d",&rent);
    printf("Enter Transport Allowance:");
    scanf("%d",&transport);
    printf("Enter FBP Allowance:");
    scanf("%d",&fbp);
    printf("Enter Income tax:");
    scanf("%d",&incometax);
    printf("Enter Provident Fund:\n");
    scanf("%d",&fund);
    // Calculating Gross salary excluding Income tax and Provident Fund
    gross = basic+rent+transport+fbp+bonus;
    printf("Gross Salary:%d", gross);
}
