#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        long long int x,n;
        scanf("%lld %lld", &x, &n);
        /*long long int pres = x;
        for (int i=1; i<=n; i++){
            if(pres%2 == 0){
                pres -= i;
            }
            else{
                pres += i;
            }
        }
        printf("%lld\n", pres);*/
        if(n%2==1){
            if(x%2==0){
                if(n%4 == 3){
                    printf("%lld\n", x+n+1);
                }
                else{
                    printf("%lld\n", x-n);
                }
            }
            else{
                if(n%4 == 3){
                    printf("%lld\n", x-n-1);
                }
                else{
                    printf("%lld\n", x+n);
                }
            }
        }
        else if(n>0 && n%2==0){
            if(x%2==1){
                if(n%4 == 2){
                    printf("%lld\n", x-1);
                }
                else{
                    printf("%lld\n", x);
                }
            }
            else{
                if(n%4 == 0){
                    printf("%lld\n", x);
                }
                else{
                    printf("%lld\n", x+1);
                }
            }
        }
        else{
            printf("%lld\n", x);
        }
    }
    return 0;
}