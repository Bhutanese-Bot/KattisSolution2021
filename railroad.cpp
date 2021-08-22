#include<bits/stdc++.h>
#define endl "\n"
using namespace std;
int main(void)
{
	int junctions,switches;
	cin >> junctions >> switches;
	if(switches != 0)
	{
		if(switches % 2 == 0 && junctions < switches)
		{
			cout << "possible" << endl;
		}else
		{
			cout << "impossible" << endl;
		}
	}else{
	cout << "possible" << endl;
	}
}