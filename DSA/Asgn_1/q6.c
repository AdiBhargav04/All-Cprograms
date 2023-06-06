#include<stdio.h>
void Create(int[],int);
void Display(int[],int);
void Search(int[],int);
int main()
{
    int n,Arr[50];
    printf("Enter no of elements you want to enter: ");
    scanf("%d",&n);
    Create(Arr,n);
    printf("Array:\n");
    Display(Arr,n);
    Search(Arr,n);
    return 0;
}
void Create(int Arr[50],int n)
{
    int i=0;
    for(i=0;i<n;i++)
    {
        printf("Enter element: ");
        scanf("%d",&Arr[i]);
    }
}
void Display(int Arr[50],int n)
{
    int i=0;
    for(i=0;i<n;i++)
    {
        printf("%d\t",Arr[i]);
    }
    printf("\n");
}
void Search(int Arr[50],int n)
{
    int i=0,key,ctr=0;
    printf("Enter element you want to search: ");
    scanf("%d",&key);
    for(i=0;i<n;i++)
    {
        if(key==Arr[i])
        {
            ctr=1;
        }
    }
    if(ctr==1)
    {
        printf("Element found\n");
    }
    else 
    {
        printf("Element not found\n");
    }
}