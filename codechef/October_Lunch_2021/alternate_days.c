#include<stdio.h>
#include<stdlib.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int a,b,p,q;
        scanf("%d %d %d %d", &a, &b, &p, &q);
        if(p%a == 0 && q%b == 0){
            if(abs((p/a)-(q/b)) < 2){
                printf("YES\n");
            }
            else
                printf("NO\n");
        }
        else
            printf("NO\n");
    }
    return 0;
}