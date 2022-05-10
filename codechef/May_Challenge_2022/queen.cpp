#include<iostream>

using namespace std;

int max(int a, int b){
    if(a>b){
        return a;
    }
    return b;
    // return a ? a > b : b;
}

int min(int a, int b){
    if (a<b)
        return a;
    return b;
    // return a ? a < b : b;
}

int main(){
    int t;
    cin >> t;
    while(t>0){
        int n,x,y;
        cin >> n >> x >> y;
        int ans = 0;
        ans += 2*(n-1);
        ans += n - max(x,y);
        ans += min(x,y) - 1;
        ans += min(n -x, y-1);
        ans += min(n -y, x-1);
        cout << ans << endl;
        t--;
    }
    return 0;
}