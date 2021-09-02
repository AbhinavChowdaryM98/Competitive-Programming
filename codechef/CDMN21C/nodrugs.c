#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n,k,l,max=0;
        scanf("%d %d %d", &n, &k, &l);
        int arr[n];
        for(int i=0; i<n; i++){
            scanf("%d", &arr[i]);
            if(arr[i]>max){
                max = arr[i];
            }
        }
        if(max>arr[n-1] && k<=0){
            printf("No\n");
        }
        else if(k<=0 && arr[n-1]==max){
            printf("Yes\n");
        }
        else{
            int tmp = max - arr[n-1];
            tmp = (tmp/k) + 1;
            if(tmp>=l){
                printf("No\n");
            }
            else{
                printf("Yes\n");
            }
        }
    }
}