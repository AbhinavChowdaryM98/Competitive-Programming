#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0){
        int n;
        cin >> n;
        int a1 = 0, a2 = 0;
        for (int i=0; i<3; i++){
            a2 += n%10;
            n = n/10;
        }
        for (int i=0; i<3; i++){
            a1 += n%10;
            n = n/10;
        }
        if(a1 == a2){
            cout << "Yes\n";
        }
        else{
            cout << "No\n";
        }
        t--;
    }
    return 0;
}