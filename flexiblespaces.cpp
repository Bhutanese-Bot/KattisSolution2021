#include<bits/stdc++.h>
using namespace std;
#define pb push_back
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	int tot_spc,partitions;
	cin >> tot_spc >> partitions;
	vector<int> part;
	part.pb(tot_spc);
	while(partitions--)
	{
		int p;
		cin >> p;
		part.pb(p);
	}
	set<int>spaces;
	for(auto i:part)
	{
		int f = i-0;
		spaces.insert(f);
		for(auto ans:part)
		{
			if(ans == i)
			{
				continue;	
			}else{
				int spc = i - ans;
				if(spc>0)
				{
				spaces.insert(spc);
				}
			}
		}
	}
	for(auto key:spaces)
	{
		cout << key << " ";
	}
	return 0;
}	