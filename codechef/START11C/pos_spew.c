#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n,k;
        scanf("%d %d", &n, &k);
        int arr[n];
        int cop_arr[n];
        for (int i=0; i<n; i++){
            scanf("%d", &arr[i]);
            cop_arr[i]=arr[i];
        }
        for(int i=0;i<k;i++){
            for(int j=0;j<n;j++)
            {
                if(arr[j]>0){
                    cop_arr[(j+1)%n]++;
                    if(j==0)
                        cop_arr[(n-1)]++;
                    else
                        cop_arr[j-1]++;
                }
            }
            for (int j = 0; j < n; j++)
            {
                arr[j] = cop_arr[j];
            }
        }
        int sum=0;
        for (int i = 0; i < n; i++)
        {
            sum+=arr[i];
        }
        printf("%d\n", sum);
    }
    return 0;
}