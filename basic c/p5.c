#include<stdio.h>
int main()
{
    int n;
    printf("Enter a value: ");
    scanf("%d",&n);
    if(n%11==0 && n%13==0)
        printf("divisible \n");
    else
        printf("not divisible\n");
    return 0;
}