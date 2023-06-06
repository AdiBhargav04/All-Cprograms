#include<stdio.h>
int main()
{
    int a,b,c,d,e,avg;
    printf("Enter marks");
    scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
    avg=(a+b+c+d+e)/5;
    if(avg>=60)
        printf("first");
    else if(avg>=50 && avg<60)
        printf("second");
    else if(avg>=40 && avg<50)
        printf("third");
    else if(avg<40)
        printf("fail");
    return 0;
}