#include <stdio.h>

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		long long int n;
		long long int answer=0;
		scanf("%lld", &n);
		long long int s[n],min_i[n],min_index=0;
		scanf("%lld", &s[0]);
		min_i[0] = s[0];
		for(int i=1;i<n;i++)
		{
			scanf("%lld", &s[i]);
			if(min_i[i-1]>s[i]){
				min_i[i] = s[i];
				min_index = i;
			}
			else
				min_i[i] = min_i[i-1];
		}
		long long int tmp = min_index;
		answer+= (n - min_index)*s[min_index];
		tmp--;
		while(tmp>=0)
		{
			long long int cpy = tmp;
			while(min_i[cpy]==min_i[cpy-1])
				cpy--;
			answer+=(tmp-cpy+1)*min_i[cpy];
			tmp = cpy-1;
		}
		printf("%lld\n", answer);
	}
	return 0;
}
