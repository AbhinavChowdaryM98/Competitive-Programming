#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int x,y;
        scanf("%d %d", &x, &y);
        if(x>=y){
            printf("%d\n", x-y);
        }
        else{
            int tmp = y - x, ans = tmp/2;
            ans += (tmp%2)*2;
            printf("%d\n", ans);
        }
    }
    return 0;
}