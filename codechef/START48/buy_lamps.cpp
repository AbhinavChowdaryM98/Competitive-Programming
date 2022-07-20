#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0){
        int n,k,x,y;
        cin >> n >> k >> x >> y;
        if(x<=y){
            cout << n*x << endl;
        }
        else{
            cout << k*x + (n-k)*y << endl;
        }
        t--;
    }
    return 0;
}