#include <stdio.h>

int minimum(int a, int b){
	return (a<b ? a : b);
}

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		int n,res=0;
		scanf("%d", &n);
		int arr[n],max[n];
		for(int i=0;i<n;i++)
			scanf("%d", &arr[i]);
		max[0]=arr[0];
		res++;
		for(int i=1;i<n;i++){
			max[i] = minimum(max[i-1],arr[i]);
			if(max[i]==arr[i])
				res++;
		}
		printf("%d\n",res);
	}
	return 0;
}
