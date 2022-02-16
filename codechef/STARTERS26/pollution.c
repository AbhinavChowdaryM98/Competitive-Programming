#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int x,y,n, poll=0;
        scanf("%d %d %d", &n, &x, &y);
        if(n > 100){
            if(x < y*25){
                poll += ((int)n/100)*x;
                n = n%100;
                if(x < y*((int)((n+3)/4))){
                    poll+=x;
                }
                else{
                    poll += y*((int)((n+3)/4));
                }
            }
            else{
                poll += y*((int)((n+3)/4));
            }
        }
        else{
            if(x < y*((int)((n+3)/4))){
                poll+=x;
            }
            else{
                poll += y*((int)((n+3)/4));
            }
        }
        printf("%d\n", poll);
    }
}