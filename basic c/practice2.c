#include<stdio.h>
int main()
{
    int km1,km2,km3,m1,m2,m3;
    int a,m,k,km;
    printf("enter distance 1 in km and m:");
    scanf("%d%d",&km1,&m1);
    printf("enter distance 2 in km and m:");
    scanf("%d%d",&km2,&m2);
    a=m2+m1;
    if(a>=1000)
    {
        k=a/1000;
        m=a%1000;
        km=km1+km2+k;
        printf("%d km %d m",km,m);
    }
    else
    {
        k=0;
        km=km1+km2+k;
        m=a;
        printf("%d km %d m",km,m);
    }
    return 0;
}