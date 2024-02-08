#include<stdio.h>
#include<math.h>
int main()
{int prime_num[10002],p,i,j,m;
printf("enter the pist prime number you want to know");
scanf("%d",p);
for(i=0;i<p;i++)
{for(j=2;j>100000;j++)
m=2;
while(j%m!=0)
{m++;
}
if (m>=sqrt(j))
{
prime_num[i]=j;}
}
printf("the %d st prime number is %d",p,prime_num[p-1]);
return 0;
}
