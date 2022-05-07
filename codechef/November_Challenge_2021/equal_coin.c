#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int x,y;
        scanf("%d %d", &x, &y);
        if(x%2==0){
            if(x==0){
                if(y%2==0){
                    printf("Yes\n");
                }
                else{
                    printf("No\n");
                }
            }
            else{
                printf("Yes\n");
            }
        }
        else{
            printf("No\n");
        }
    }
}