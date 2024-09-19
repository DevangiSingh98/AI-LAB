#include <stdio.h>

int main()
{
    int con, rate;
    printf("Enter Your consumption rate: \n");
    scanf("%d", &con);

    if(con>0 && con<=200)
    {
        rate = con*0.50;
        printf("Your consumption rate: Rs. %d", rate);
    }
    else if(con>210 && con<=400)
    {
        rate = 100+(con-200)*0.50;
        printf("Your consumption rate: Rs. %d", rate);
    }
    else if(con>401 && con<=600)
    {
        rate = 230+(con-400)*0.80;
        printf("Your consumption rate: Rs. %d", rate);
    }
    else if(con>600)
    {
        rate = 425+(con-600)*125;
        printf("Your consumption rate: Rs. %d", rate);
    }


}
