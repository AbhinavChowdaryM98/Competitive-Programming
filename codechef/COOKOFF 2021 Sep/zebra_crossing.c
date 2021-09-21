#include<stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, k, max_k=0;
        scanf("%d %d", &n, &k);
        char cross[n];
        scanf("%s", cross);
        char prev = cross[0];
        for (int i = 1; i < n; i++)
        {
            if(prev != cross[i]){
                max_k++;
                prev = cross[i];
            }
        }
        char final = cross[n-1];
        int final_prev;
        for (int i = n-1; i >= 0; i--)
        {
            if(final != cross[i]){
                final_prev = i;
                break;
            }
        }
        if (max_k < k)
        {
            printf("-1\n");
        }
        else{
            if(k%2==0){
                (cross[0] == cross[n-1]) ? printf("%d\n", n) : printf("%d\n", final_prev+1);
            }
            else{
                (cross[0] != cross[n-1]) ? printf("%d\n", n) : printf("%d\n", final_prev+1);
            }
        }
    }
    
}