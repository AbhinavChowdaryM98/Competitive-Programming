#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int l,r;
        scanf("%d %d", &l, &r);
        if(l==r){
            printf("0\n");
        }
        else if(r - l < l){
            printf("%d\n", (r - l));
        }
        else{
            int tmp;
            if(r%2==0){
                tmp = (r/2)+1;
            }
            else {
                tmp = r+1;
                tmp = tmp/2;
            }
            printf("%d\n", r%tmp);
        }
    }
    return 0;
}