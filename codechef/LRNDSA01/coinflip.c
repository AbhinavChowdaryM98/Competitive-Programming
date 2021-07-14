#include <stdio.h>

int reverse(int a){
	return (a==2 ? 1 : 2);
}

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		int g;
		scanf("%d", &g);
		while(g--)
		{
			int i,n,q,count=0;
			scanf("%d %d %d", &i, &n, &q);
			/*int arr[n];
			if(n%2==0){
				arr[0]=reverse(i);
				if(arr[0]==q)
					count++;
			}
			for(int j=1;j<n;j++)
				arr[j]=reverse(arr[j-1]);*/
			if(n%2==0)
			{
				printf("%d\n", n/2);
			}
			else
			{
				if(i==q)
					printf("%d\n", n/2);
				else
					printf("%d\n", n/2 + 1);
			}
		}
	}
	return 0;
}
