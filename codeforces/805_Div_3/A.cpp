#include<iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0){
        long long int n;
        cin >> n;
        long long int s = 1;
        while(s <= n){
            s *= 10;
        }
        cout << n - s/10 << endl;
        t--;
    }
    return 0;
}