#include<stdio.h>
int main()
{
    int a,b,c,d;
    float X;
    printf("Enter a,b,c,d: ");
    scanf("%d%d%d%d",&a,&b,&c,&d);
    if(c>d||c<d)
    {
        X=(a-b)/(c-d);
        printf("X:%f",X);
    }
    if(c==d)
        printf("error");
    return 0;    
}