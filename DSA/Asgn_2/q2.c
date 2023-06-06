#include<stdio.h>
int main()
{
	int n,*p;
	printf("Enter a value: ");
	scanf("%d",&n);
	p=&n;
	printf("Value is %d\n",*p);
	printf("Address is %d\n",p);
	return 0;
}
