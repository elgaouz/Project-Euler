#include<stdio.h>
#include<math.h>
int main()
{long int n;
long int j;
long int i;
 int c=0;
printf("entrer un entier");
scanf("%ld",&n);
for(j=2;j<=2000000;j++)
{i=2;
while((j%i!=0)&&i<sqrt(j)+1)
{i+=1;}
if(i>=sqrt(j)+1)
{c+=j;}
}
printf("the sum of the primes below  est %d",c);
return 0;
}

