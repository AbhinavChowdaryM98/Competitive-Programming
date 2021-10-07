#include<stdio.h>

int main(){
    long long int t;
    scanf("%lld", &t);
    while(t--){
        long long int n;
        long long int ans = 0;
        scanf("%lld", &n);
        long long int cpy = n, tmp = n&(n-1);
        if(n==1){
            printf("1\n");
        }
        else if(tmp == 0){
            printf("%lld\n", n/2);
        }
        else{
            while (n != 1)
            {
                n = n/2;
                ans++;
            }
            ans = 1<<ans;
            printf("%lld\n", cpy - ans + 1);
        }
    }
    return 0;
}