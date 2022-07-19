#include<bits/stdc++.h>

using namespace std;

int main()
{
	map<int, vector<int>> a;
	a.insert(pair<int, int> (1, 10));
	a.insert(pair<int, int> (1, 20));
	a.insert(pair<int, int> (1, 30));
	cout << a[1] << endl;
	return 0;
}
