#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t > 0){
        int x,y;
        cin >> x >> y;
        int ans = 0;
        if(x < y){
            ans = (y-x);
        }
        else{
            ans = (x - y)/2 + 2*((x-y)%2);
        }
        // ans++;
        cout << ans << endl;
        t--;
    }
}