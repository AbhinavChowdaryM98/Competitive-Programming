#include <stdio.h>

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--){
		int n;
		scanf("%d", &n);
		char str[2*n];
		scanf("%s", str);
		int a[2]={0,0},b[2]={0,0},ans=2*n;
		for(int i=0;i<2*n;i++)
		{
			//int tmp = (int)str[i];
			//printf("tmp:%d\n", tmp);
			if(i%2==0)
				a[(int)str[i]-48]++;
			else
				b[(int)str[i]-48]++;
			//printf("a:\t0:%d\t1:%d\n", a[0], a[1]);
			//printf("b:\t0:%d\t1:%d\n", b[0], b[1]);
			if(n - a[1] < b[0] || n - b[1] < a[0]){
				ans = i+1;
				break;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
