#include<stdio.h>
int main()
{
    int a[3][3], MIN, MAX;          //declaration
    //user input
    printf("enter matrix: ");

    for(int i = 0 ;  i < 3; i++)
    {
        for(int j = 0 ; j < 3 ; j++ )        //reading the 3X3 matrix
        {
            scanf("%d",&a[i][j]);
        }    
    }

    printf("Matrix: \n");
    for(int i = 0 ;  i < 3; i++)
    {
        for(int j = 0 ; j < 3 ; j++ )        //reading the 3X3 matrix
        {
            printf("%d \t",a[i][j]);
        }
        printf("\n");    
    }

    MIN = MAX = a[0][0];

    for(int i = 0 ; i < 3 ; i++)
    {
        for(int j = 0 ; j < 3 ; j++)
        {
            if (a[i][j]<MIN)
            {
                MIN = a[i][j];
            }

            if (a[i][j]>MAX)
            {
                MAX = a[i][j];
            }

        }
    }
    printf("\n MAX element = %d", MAX);
    printf("\n MIN element = %d", MIN);  

}