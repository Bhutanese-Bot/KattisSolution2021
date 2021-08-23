#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int testcase, width, height;
	cin >> testcase >> width >> height;
	int length = sqrt(pow(width,2)+pow(height,2));
	while(testcase--)
	{
		int check;
		cin >> check;
		if(check <= length) cout << "DA" << "\n";
		else cout << "NE" << "\n";
	}
  return 0;
	}
