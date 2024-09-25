#include<stdio.h>
int main()
{
    int i,j,n;    //declaration
    char ch;
    ch = 'A';  

    //User input      
    printf("Enter n: ");
    scanf("%d",&n);

    for(i=1 ; i <= n ; i++)
    {
        for(j=1; j <= i ; j++)          //inner loop for printing the letters
        {
            printf("%c",ch);
        }
        printf("\n");     //new line

        ch += 1;       //Increment of letter


    }
    return 0;
}