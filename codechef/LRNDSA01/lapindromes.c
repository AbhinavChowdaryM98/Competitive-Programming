#include <stdio.h>
#include<string.h>

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		char str[1003];
		scanf("%s", str);
		int len = strlen(str),tmp[257];
		for(int i=1;i<=256;i++)
			tmp[i]=0;
		for(int i=0;i<(len/2);i++)
			tmp[(int)str[i]]++;
		for(int i=(len/2)+(len%2);i<len;i++)
			tmp[(int)str[i]]--;
		int temp=1;
		for(int i=0;i<len;i++)
			if(tmp[(int)str[i]]!=0){
				temp=0;
				break;
			}
		if(temp==1)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
