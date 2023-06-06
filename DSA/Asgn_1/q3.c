#include<stdio.h>
void Create(int[],int);
void Display(int[],int);
void Copied(int[],int);
int main()
{
    int n,Arr1[50];
    printf("Enter no of elements you want to enter: ");
    scanf("%d",&n);
    Create(Arr1,n);
    printf("Original Array\n");
    Display(Arr1,n);
    printf("Copied Array\n");
    Copied(Arr1,n);
    return 0;
}
void Create(int Arr1[50],int n)
{
    int i=0;
    for(i=0;i<n;i++)
    {
        printf("Enter element: ");
        scanf("%d",&Arr1[i]);
    }
}
void Display(int Arr1[50],int n)
{
    int i=0;
    for(i=0;i<n;i++)
    {
        printf("%d\t",Arr1[i]);
    }
    printf("\n");
}
void Copied(int Arr1[50],int n)
{
    int i=0,Arr2[50];
    for(i=0;i<n;i++)
    {
        Arr2[i]=Arr1[i];
    }
    for(i=0;i<n;i++)
    {
        printf("%d\t",Arr2[i]);
    }
    printf("\n");
}