#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0){
        int l,r,a;
        cin >> l >> r >> a;
        if(r%a != 0){
            int tmp = r/a;
            int val1 = tmp + r%a, val2 = tmp-1+a-1;
            if(l < tmp*a){
                cout << (val1 > val2 ? val1:val2) << endl;
            }
            else{
                cout << val1 << endl;
            }
        }
        else{
            int tmp = r/a;
            int val1 = tmp, val2 = tmp-1+a-1;
            if(l < tmp*a){
                cout << (val1 > val2 ? val1:val2) << endl;
            }
            else{
                cout << val1 << endl;
            }
        }
        t--;
    }
}