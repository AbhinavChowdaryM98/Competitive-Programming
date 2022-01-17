#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int a,b,c;
        cin >> a >> b >> c;
        int d1 = b - a, d2 = c - b, d3 = c - a;
        if(b+d1 >= c){
            if((b+d1)%c==0){
                printf("YES\n");
                continue;
            }
        }
        if(b - d2 >= a){
            if((b-d2)%a==0){
                printf("YES\n");
                continue;
            }
        }
        if((abs(d3))%2 == 0){
            if((a+((d3)/2))%b==0){
                printf("YES\n");
                continue;
            }
        }
        printf("NO\n");
    }
    return 0;
}