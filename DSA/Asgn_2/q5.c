#include<stdio.h>
void fac(int*);
int main()
{
	int a,*p;
	printf("Enter a number: ");
	scanf("%d",&a);
	p=&a;
	fac(p);
	return 0;
}
void fac(int *p)
{
	int f=1,i=1;
	for(i=1;i<=*p;i++)
	{
		f=f*i;
	}
	printf("Factorial of the number is %d\n",f);
}
