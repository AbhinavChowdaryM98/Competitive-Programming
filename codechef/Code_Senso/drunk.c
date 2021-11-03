#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int k;
        scanf("%d", &k);
        int ans = 0;
        ans = (int)(k/2);
        ans = ans*2;
        ans += 3*(k%2);
        printf("%d\n", ans);
    }
    return 0;
}