#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int clerks;
	cin >> clerks;
	int arr[clerks];
	for(int i=0; i<clerks; ++i)
	{
		int order;
		cin >> order;
		arr[i] = order;
	}
	int count =0;
	for(int i=1; i<clerks; ++i)
	if(arr[i] < arr[i-1]) count += 1;
	cout << count+1;
}
