#include<stdio.h>
void Create(int[],int);
void Display(int[],int);
void Insert(int[],int);
int main()
{
    int n,Arr[50];
    printf("Enter no of elements you want to enter: ");
    scanf("%d",&n);
    Create(Arr,n);
    printf("Array:\n");
    Display(Arr,n);
    Insert(Arr,n);
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
void Insert(int Arr[50],int n)
{
    int key,in,i=0;
    printf("Enter element you want to insert: ");
    scanf("%d",&key);
    printf("Enter the index at which you want you to enter the element: ");
    scanf("%d",&in);
    for(i=n;i>=in-1;i--)
    {
        Arr[i+1]=Arr[i];
    }
    Arr[in]=key;
    for(i=0;i<n+1;i++)
    {
        printf("%d\t",Arr[i]);
    }
    printf("\n");
}