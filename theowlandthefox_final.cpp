#include<bits/stdc++.h>
#define ll long long
using namespace std;
int modulo_sum(int n)
{
	return n == 0?0:n%10+modulo_sum(n/10);
}
int main()
{
	ll testcase;
	cin >> testcase;
	while(testcase--)
	{
		ll number;
		scanf("%ld",&number);
		int real_sum =modulo_sum(number)-1;
		while(number--)
		{
			if(real_sum == modulo_sum(number))
			{
				cout << number << "\n";
				break;
			}
		}
}
}
