#include<bits/stdc++.h>
using namespace std;
#define LLI long long int
#define SSD(x) scanf("%lld",&x)
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	while(1)
	{
	    LLI N,M;
	    cin >>N>>M;
	    if(N == 0 and M== 0) break;
		bitset<10000000>Jack;
		bitset<10000000>Jill;
		for(int i=0;i<N; i++)
		{
			LLI pos;
			cin >> pos;
			Jack[pos] = true;
		}
		for(int j=0; j<M; ++j)
		{
			LLI pos;
			cin>>pos;
			Jill[pos] = true;
		}
		cout<<(Jack&Jill).count()<<"\n";
	}
}
