#include<stdio.h>
int main()
{
    char str[50];
    int i=0,countc=0,countw=0;
    printf("enter the string");
    scanf("%[^\n]",str);
    while(str[i]!='\0')
    {
        countc++;
        if(str[i]=='\0')
        {         
            countw++;
            i++;
        }
    printf("string length=%d\n no. of words=%d",countc,countw+1);
    }
}