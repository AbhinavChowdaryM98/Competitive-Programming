#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int x,y,z;
        scanf("%d %d %d", &x, &y, &z);
        if(y - x > 2*z)
            printf("NO\n");
        else{
            printf("YES\n");
        }
    }
    return 0;
}