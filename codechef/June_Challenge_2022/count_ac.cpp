#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t>0){
	    int p;
	    cin >> p;
        int h = p/100, o = p%100;
        if (h + o <= 10){
            cout << h+o << endl;
        }
        else{
            cout << -1 << endl;
        }
	    t--;
	}
	return 0;
}