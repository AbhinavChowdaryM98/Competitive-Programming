#include<iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0)
    {
        int n,k;
        cin >> n >> k;
        if(k==0){
            if(n%4 == 0){
                cout << "Off" << endl;
            }
            else{
                cout << "On" << endl;
            }
        }
        else{
            if(n==0){
                cout << "On" << endl;
            }
            else{
                cout << "Ambiguous" << endl;
            }
        }
        t--;
    }
}