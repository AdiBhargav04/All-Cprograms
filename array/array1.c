#include<stdio.h>
int main()
{
    int a[10][10],i=0,j=0,r,c,b[10][10],L[10][10];

    printf("Enter order of matrix:\n");
    scanf("%d%d",&r,&c);
    for (i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("Enter matrix element A%d%d: ",i,j);
            scanf("%d",&a[i][j]);
        }
    }
    printf("Matrix A: \n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d\t",a[i][j]);
        }
        printf("\n");
    }
    for (i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("Enter matrix element B%d%d: ",i,j);
            scanf("%d",&b[i][j]);
        }
    }
    printf("Matrix B: \n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            printf("%d\t",b[i][j]);
        }
        printf("\n");
    }
    printf("\nResultant Matrix L: \n");
    for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        {
            L[i][j]=a[i][j]+b[i][j];
            printf("%d\t",L[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    return 0;
}