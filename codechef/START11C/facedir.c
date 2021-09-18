#include<stdio.h>

int main(){
    int t;
    char* arr[]={"North","East","South","West"};
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        n = n%4;
        printf("%s\n", arr[n]);
    }
    return 0;
}