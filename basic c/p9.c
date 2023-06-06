#include<stdio.h>
int main()
{
    int a,b,c;
    printf("Enter 3 no.s: ");
    scanf("%d%d%d",&a,&b,&c);
    if(a>b && a>c)
    {
        printf("%d is the greatest",a);
        if(b<c)
            printf("%d is smallest",b);
        else   
            printf("%d is smallest",c);
    }
    if(b>c && b>a)
    {
        printf("%d is the greatest",b);
        if(a<c)
            printf("%d is smallest",a);
        else   
            printf("%d is smallest",c);
    }
    if(c>a && c>b)
    {
        printf("%d is the greatest",c);
        if(a<b)
            printf("%d is smallest",a);
        else   
            printf("%d is smallest",b);
    }
    return 0;

}