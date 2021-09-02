#include<stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    while(t--){
        int arr[2][3],one_s[]={0,0};
        for(int i=0;i<2;i++)
        {
            for(int j=0;j<3;j++){
                scanf("%d", &arr[i][j]);
                if(arr[i][j]==1){
                    one_s[i]++;
                }
            }
        }
        if(one_s[0]==one_s[1]){
            printf("Pass\n");
        }
        else{
            printf("Fail\n");
        }
    }
    return 0;
}