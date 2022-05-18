#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t){
        int n,x;
        cin >> n >> x;
        int arr[n];
        for (int i=0; i<n; i++){
            cin >> arr[i];
        }
        int* c = std::max_element(arr, arr+n);
        int s = 0;
        for (int i=0; i<n;i++){
            s += (int) ((arr[i]-1)/x);
        }
        s+=n;
        cout << std::min(*c, s) << endl;
        t--;
    }
    return 0;
}