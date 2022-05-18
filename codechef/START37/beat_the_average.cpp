#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t){
        int n,m,x;
        cin >> n >> m >> x;
        if(m==x){
            cout << 0 << endl;
        }
        else{
            int k = n-1;
            for (;k>0;k--){
                if(k*(x+1) < n*x){
                    break;
                }
            }
            cout << k << endl;
        }
        t--;
    }
}