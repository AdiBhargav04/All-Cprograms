#include<stdio.h>
int main()
{
	int l,b,*p,*q,area,peri;
	printf("Enter length and breadth of rectangle: ");
	scanf("%d%d",&l,&b);
	p=&l;
	q=&b;
	area=(*p)*(*q);
	peri=2*((*p)+(*q));
	printf("Area is %d and Perimeter is %d\n",area,peri);
	return 0;
}
