#include<stdio.h>
int main()
{
    int r,c1,c2;
    for (r=1,r<=5,r++)
    {
        for(c1=4,c1>=r,c1--)
        {
            printf(" ");
            for(c2=1,c2<=4,c2++)
            {
                printf("%d",c2);

            }
            printf("\n");
        }
    }
    return 0;
}