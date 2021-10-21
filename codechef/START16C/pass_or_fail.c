#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n,x,p;
        scanf("%d %d %d", &n, &x, &p);
        int marks = 3*n - 4*(n-x);
        if(marks>=p){
            printf("Pass\n");
        }
        else{
            printf("Fail\n");
        }
    }
    return 0;
}