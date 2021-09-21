#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        int arr[n], cnt=0;
        for(int i=0; i<n; i++){
            scanf("%d", &arr[i]);
            if(arr[i]%2 != 0)
                cnt++;
        }
        if(cnt==n || cnt == 0){
            printf("-1\n");
        }
        else{
            for (int i = 0; i < n; i++)
            {
                if(arr[i]%2==1){
                    printf("%d ", arr[i]);
                }
            }
            for (int i = 0; i < n; i++)
            {
                if(arr[i]%2 == 0){
                    printf("%d ", arr[i]);
                }
            }
            printf("\n");
        }
    }
    return 0;
}