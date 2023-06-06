#include <stdio.h>
void Create(int[], int);
void Display(int[], int);
int class_max(int[], int);
int class_min(int[], int);
int class_sum(int[], int);
int class_avg(int[], int);
int main()
{
    int n, Arr[50];
    printf("Enter no of elements you want to enter: ");
    scanf("%d", &n);
    Create(Arr, n);
    printf("Array of marks secured:\n");
    Display(Arr, n);
    class_max(Arr, n);
    class_min(Arr, n);
    class_sum(Arr, n);
    class_avg(Arr, n);
    return 0;
}
void Create(int Arr[50], int n)
{
    int i = 0;
    for (i = 0; i < n; i++)
    {
        printf("Enter element: ");
        scanf("%d", &Arr[i]);
    }
}
void Display(int Arr[50], int n)
{
    int i = 0;
    for (i = 0; i < n; i++)
    {
        printf("%d\t", Arr[i]);
    }
    printf("\n");
}
int class_max(int Arr[50], int n)
{
    int i = 0,max;
    max = Arr[0];
    for (i = 0; i <n; i++)
    {
        if (Arr[i] > max)
        {
            max = Arr[i];
        }
    }
    printf("Maximum amongst:%d\n", max);
}
int class_min(int Arr[50], int n)
{
    int i = 0,min;
    min = Arr[0];
    for (i = 0; i<n; i++)
    {
        if (Arr[i] < min)
        {
            min = Arr[i];
        }
    }
    printf("Maximum amongst:%d\n", min);
}
int class_sum(int Arr[50],int n)
{
    int sum=0,i=0;
    for(i=0;i<n;i++)
    {
        sum+=Arr[i];
    }
    printf("Total Marks:%d\n",sum);
}
int class_avg(int Arr[50],int n)
{
    int sum=0,m=0;
    for(m=0;m<n;m++)
    {
        sum+=Arr[m];
    }
    printf("Average of this array:%d\n",sum/n);
}