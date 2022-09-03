#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t > 0){
        int n;
        cin >> n;
        // char s1[n], s2[n];
        // cin.getline(s1, n);
        // cin.getline(s2, n);
        string s1, s2;
        getline(cin, s1);
        getline(cin, s2);
        cout << s1 << endl;
        cout << s2 << endl;
        int flag = 1;
        for (int i=0; i<n; i++){
            if(s1[i] == 'R'){
                if(s1[i] != s2[i]){
                    flag = 0;
                    break;
                }
            }
        }
        if(flag){
            cout << "Yes\n";
        }
        else{
            cout << "No\n";
        }
        t--;
    }
    return 0;
}