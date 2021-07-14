#include <stdio.h>

int minimum(int a, int b){
	return (a<b ? a : b);
}

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		//int cpy = n;
		int res=0;//twos=0,fives=0;
		/*while(n>=5)
		{
			cpy = n;
			while(cpy%10==0){
				res++;
				cpy = cpy/10;
			}
			while(cpy%5==0)
			{
				fives++;
				cpy = cpy/5;
			}
			while(cpy%2==0)
			{
				twos++;
				cpy = cpy/2;
			}
			while(twos>0 && fives>0)
			  {
			  int tmp = minimum(twos,fives);
			  res+=tmp;
			  twos-=tmp;
			  fives-=tmp;
			  }
			n--;
		}
		int tmp = minimum(twos,fives);
		res+=tmp;
		twos-=tmp;
		fives-=tmp;*/
		for(int i=5; n/i>=1; i*=5)
			res+= n/i;
		printf("%d\n", res);
	}
	return 0;
}
