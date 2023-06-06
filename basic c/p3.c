#include<stdio.h>
int main()
{
    int a,b;
    float c;
    printf("Enter a Floating value: ");
    scanf("%f",&c);

    b=c+1;
    a=c;

    printf("Floor value:%d\n",a);
    printf("Ceiling value:%d",b);
    return 0;
}