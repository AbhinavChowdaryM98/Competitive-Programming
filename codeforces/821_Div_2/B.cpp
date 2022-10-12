#include<iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--){
        int n,x,y;
        cin >> n >> x >> y;
        if((x != 0 && y != 0) || (x == 0 && y == 0)){
            cout << -1 << endl;
        }
        else{
            if((n-1)%(x+y) != 0){
                cout << -1 << endl;
            }
            else{
                int arr[n-1], ans = (n-1)/(x+y), i=0, flag=0;
                while(i<(n-1)){
                    int win = i+1;
                    if(flag)
                        win++;
                    for (int j=0; j<(x+y); j++){
                        arr[i+j] = win;
                    }
                    i = i+(x+y);
                    flag = 1;
                }
                for (int i=0; i< (n-1); i++){
                    cout << arr[i] << " ";
                }
                cout<<endl;
            }
        }
    }
    return 0;
}