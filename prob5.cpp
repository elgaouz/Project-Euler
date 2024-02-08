#include<stdio.h>
int smallest_multiple(int l[],int n)
{int m=1;
int i;
while(1){
for(i=0;i<n;i++)
  {if (m%l[i]!=0)
     {m+=1;}
  }}
return m;
}
int main()
{int l[3]={1,2,3};
int n;
printf("the smallest number divisible by all of the numbers from 1 to 20 is %d",smallest_multiple(l,20));
return 0;
}

