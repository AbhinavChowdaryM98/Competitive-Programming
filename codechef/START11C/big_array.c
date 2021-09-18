#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        long long int n,s;
        scanf("%lld %lld", &n, &s);
        long long int tmp = n*(n+1);
        tmp = tmp/2;
        if(tmp<=s){
            printf("-1\n");
        }
        else if(tmp-s > n){
            printf("-1\n");
        }
        else{
            printf("%lld\n", tmp-s);
        }
    }
    return 0;
}