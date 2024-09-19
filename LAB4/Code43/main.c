#include <stdio.h>

int main()
{
    int com,sales;     //defining the variables
    //user input
    printf("Enter your sales amount: ");
    scanf("%d",&sales);

    // Calculating commission for different sales amount

    if (sales<=500)
    {
        com=sales/20;
    }
    else if (sales>500 && sales<=2000)
    {
        com=35+sales/10;
    }
    else if (sales>2000 && sales<=5000) {
        com=185 + sales*3/25;
    }
    else if (sales>5000){
        com=sales/8;
    }
    else {
        printf("Invalid amount");
    }
    printf("The commission obtained by the sales representative is =  %d ",com);
    return 0;
}
