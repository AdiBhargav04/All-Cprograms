#include<stdio.h>
int main() 
{
    int a[10][10], b[10][10], L[10][10], r,c, i, j, k;

    printf("Enter order of matrix: \n");
    scanf("%d%d", &r,&c);
    printf("Enter the elements of Matrix-A: \n");

    for (i = 0; i < r; i++) 
    {
        for (j = 0; j < c; j++) 
        {
            scanf("%d", & a[i][j]);
        }
    }

    printf("Enter the elements of Matrix-B: \n");

    for (i = 0; i < r; i++) 
    {
        for (j = 0; j < c; j++) 
        {
            scanf("%d", & b[i][j]);
        }
    }

    for (i = 0; i < r; i++) 
    {
        for (j = 0; j < c; j++) 
        {
            L[i][j] = 0;
            for (k = 0; k < r; k++) 
            {
                L[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    printf("The product of the two matrices is: \n");
    for (i = 0; i < r; i++) 
    {
        for (j = 0; j < c; j++) 
        {
            printf("%d\t", L[i][j]);
        }
        printf("\n");
    }
    return 0;
}
