#include<stdio.h>

int minimum(int a, int b){
    return (a<b ? a : b);
}

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n,s;
        scanf("%d %d", &n, &s);
        int t1 = minimum(n,s);
        int t2 = s - t1;
        printf("%d\n", t1-t2);
    }
    return 0;
}