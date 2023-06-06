#include<stdio.h>
int main()
/*{
    int a;
    printf("Enter a value: ");
    scanf("%d",&a);
    if (a>=0)
    {
        printf("Positive\n");
    }
    else
    {
        printf("Negative\n");
    }
    return 0;   
}*/
{
    int n,d,r,rev,m;
    printf("Enter a num: ");
    scanf("%d",&n);
    m=n;
    while(m!=0)
    {
        r=m%10;
        rev = rev*10+r;
        m=m/10;
    }
    while(rev!=0)
    {
        d=rev%10;
        switch(d)
        {
            case 1: printf("One");break;
            case 2: printf("Two");break;
            case 3: printf("Three");break;
            case 4: printf("Four");break;
            case 5: printf("Five");break;
            case 6: printf("Sex");break;
            case 7: printf("Seven");break;
            case 8: printf("Eight");break;
            case 9: printf("69");break;
            default:printf("Zero");
        }
        rev=rev/10;
    }
    return 0;
}