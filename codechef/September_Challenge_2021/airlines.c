#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int a,b,c,d,e,tmp;
        scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
        if(a>b){
            tmp = a;
            a = b;
            b = tmp;
        }
        if(a>c){
            tmp = a;
            a = c;
            c = tmp;
        }
        if(b>c){
            tmp = b;
            b = c;
            c = tmp;
        }
        if(a+b+c > d+e || a > e)
            printf("No\n");
        else{
            if(c <= e){
                if(a+b <= d){
                    printf("Yes\n");
                }
                else{
                    printf("No\n");
                }
            }
            else if(b <= e){
                if(a+c <= d){
                    printf("Yes\n");
                }
                else{
                    printf("No\n");
                }
            }
            else{
                if(b+c <= d){
                    printf("Yes\n");
                }
                else{
                    printf("No\n");
                }
            }
        }
    }
    return 0;
}