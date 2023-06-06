#include<stdio.h>
void swap(int*,int*);
int main()
{
	int a,b,*p1,*p2;
	printf("Enter value for A and B:");
	scanf("%d%d",&a,&b);
	printf("A is %d and B is %d\n",a,b);
	p1=&a;
	p2=&b;
	swap(p1,p2);
	return 0;
}
void swap(int *p1,int *p2)
{
	int c;
	c=*p1;
	*p1=*p2;
	*p2=c;
	printf("Swapped values are %d and %d\n",*p1,*p2);
}
