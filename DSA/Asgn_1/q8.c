#include<stdio.h>
void Create(int[],int);
void Display(int[],int);
void Del(int[],int);
int main()
{
    int n,Arr[50];
    printf("Enter no of elements you want to enter: ");
    scanf("%d",&n);
    Create(Arr,n);
    printf("Original Array: \n");
    Display(Arr,n);
    Del(Arr,n);
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
void Del(int Arr[50],int n)
{
    int i=0,key;
    printf("Enter the element you want to delete:");
    scanf("%d",&key);
    for(i=0;i<n;i++)
    {
        if(Arr[i]==key)
        {
            Arr[i]=Arr[i+1];
        }
    }
    for(i=0;i<n-1;i++)
    {
        printf("%d\t",Arr[i]);
    }
}