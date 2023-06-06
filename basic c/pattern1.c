#include<stdio.h>
void fib(int);
int main()
{
    int n;
    printf("Enter the limit: ");
    scanf("%d",&n);
    fib(n);
    return 0;
}
void fib(int n)
{
    int t3,t1=0,t2=1,i=0;
    t3=t1+t2;
    printf("Fibonacci Series:%d, %d, ",t1,t2);
    for(i=3;i<=n;i++)
    {
        printf("%d, ",t3);
        t1=t2;
        t2=t3;
        t3=t1+t2;
    }
}