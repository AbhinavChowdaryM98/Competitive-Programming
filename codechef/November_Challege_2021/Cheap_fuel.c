#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int x,y,a,b,k;
        scanf("%d %d %d %d %d", &x, &y, &a, &b, &k);
        int p = x + a*k, d = y + b*k;
        if(p>d){
            printf("DIESEL\n");
        }
        else if(p<d){
            printf("PETROL\n");
        }
        else{
            printf("SAME PRICE\n");
        }
    }
    return 0;
}