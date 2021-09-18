#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        if(n%2==0){
            for (int i=0; i<n; i++){
                for (int j = 0; j < n; j++)
                {
                    printf("-1 ");
                }
                printf("\n");
            }
        }
        else{
            for (int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    if(i==j){
                        printf("1 ");
                    }
                    else{
                        printf("-1 ");
                    }
                }
                printf("\n");
            }
        }
    }
    return 0;
}