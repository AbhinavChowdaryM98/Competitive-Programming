#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        (n%4 == 0) ? printf("NO\n") : printf("YES\n");
    }
    return 0;
}