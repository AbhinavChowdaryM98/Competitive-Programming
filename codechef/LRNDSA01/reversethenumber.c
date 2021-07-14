#include <stdio.h>
#include<string.h>

int main(void) {
	int t;
	scanf("%d", &t);
	while(t--)
	{
		char str[1000006];
		scanf("%s", str);
		int len = strlen(str),tmp=0;
		for(int i=len-1;i>=0;i--){
		    if(str[i]!='0'){
		        tmp=1;
		    }
		    if(tmp==1)
			    printf("%c",str[i]);
		}
		printf("\n");
	}
	return 0;
}
