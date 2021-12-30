#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int arr[7];
        for (int i=0; i<7; i++){
            scanf("%d", &arr[i]);
        }
        if(arr[2] == arr[0]+arr[1]){
            printf("%d %d %d\n", arr[0], arr[1], arr[3]);
        }
        else{
            printf("%d %d %d\n", arr[0], arr[1], arr[2]);
        }
    }
    return 0;
}