#include <iostream>
#include<utility>
#include<algorithm>

using namespace std;

int main() {
	long long int n,max=0;
	cin >> n;
	long long int arr[n];
	for(int i=0;i<n;i++)
		cin >> arr[i];
	sort(arr, arr+n);
	for(int i=0;i<n;i++)
		if(max < arr[i]*(n-i))
			max = arr[i]*(n-i);
	cout << max << endl;
	return 0;
}
