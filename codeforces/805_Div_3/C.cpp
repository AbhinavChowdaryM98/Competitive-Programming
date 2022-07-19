#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0){
        int n,k;
        cin >> n >> k;
        int ar[n];
        map <int, int> a;
        // vector <int> a[n+1];
        for (int i=0; i<n; i++){
            cin >> ar[i];
            // a[ar[i]].push_back(i);
            a.insert(pair<int, int>(ar[i], i));
        }
        for(int i = 0; i < k; i++){
            int ai,bi;
            cin >> ai >> bi;
            // if(a[ai].size() > 0 && a[bi].size() > 0){
            //     int s = a[ai][0], e = a[bi][a[bi].size() - 1];
            //     if(s < e){
            //         cout << "Yes" << endl;
            //     }
            //     else{
            //         cout << "No" << endl;
            //     }
            // }
            // else{
            //     cout << "No" << endl;
            // }
            
        }
        t--;
    }
    return 0;
}