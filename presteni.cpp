#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int testcase;
	int t = testcase;
	cin >> testcase;
	vector<int> number;
	while(testcase--)
	{
		int num;
		cin >> num;
		number.push_back(num);
	}
	int to_divide = number.at(0);
	cout << to_divide << endl;
	for(int i=1; i<number.size(); ++i)
	{
		int work = number.at(i);
		if(to_divide % work == 0)
		{
		cout << to_divide / work << "/" << "1" << endl;
		}else{
			int quotient = to_divide / work;
			int rem = to_divide % work;
			int gcd = __gcd(work,rem);
			work = work / gcd;//2
			rem = rem / gcd ;// 1
			cout << (quotient * work)+rem << "/" << work << endl;
		}
	}
	return 0;
}