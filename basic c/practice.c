#include<stdio.h>
int main()
/*
{
    int i=0,L[i],n,g,s;

    printf("no of values: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("enter value: ");
        scanf("%d",&L[i]);
    }
    printf("The Array: \n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",L[i]);
    }
    s=L[0],g=L[0];
    for(i=0;i<n;i++)
    {
        if(L[i]>g)
            g=L[i];
        if(L[i]<s)
            s=L[i];
    }
    printf("\n Smallest element:%d",s);
    printf("\n Largest element:%d",g);
    return 0;
}
*/
{
    int i=0,L[i],n,s1;
    printf("no of values: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("enter value: ");
        scanf("%d",&L[i]);
    }
    printf("The Array: \n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",L[i]);
    }
    s1=L[0];
    for(i=0;i<n;i++)
    {
        if(L[i]<L[i+1])
        {
            s1=L[i+1];
        }
    }
    printf("\nSecond smallest no:%d",s1);
    return 0;
}


