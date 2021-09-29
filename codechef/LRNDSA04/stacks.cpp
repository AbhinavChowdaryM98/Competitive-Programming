#include<iostream>
#include<stack>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t>0){
        int n;
        cin >> n;
        stack<int> tmp_stack[n];
        int arr[n];
        for (int i=0; i<n; i++){
            cin >> arr[i];
        }
        int l=0;
        tmp_stack[l].push(arr[0]);
        for (int i=1; i<n; i++){
            int min=1000000007, min_i = -1;
            for(int j=0; j<=l; j++){
                if(tmp_stack[j].top()>arr[i]){
                    if(min > tmp_stack[j].top()){
                        min = tmp_stack[j].top();
                        min_i = j;
                    }
                }
            }
            if(min_i==-1){
                tmp_stack[l+1].push(arr[i]);
                l++;
            }
            else{
                tmp_stack[min_i].push(arr[i]);
            }
        }
        cout << l+1 << " ";
        for (int i=0; i<=l; i++)
            cout << tmp_stack[i].top() << " ";
        cout << endl;
        for(int i=0; i<=l;i++){
            while(!tmp_stack[i].empty()){
                tmp_stack[i].pop();
            }
        }
        t--;
    }
    return 0;
}