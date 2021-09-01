//had hard time taking care of the data type and in vain when finding the correct solutions.
#include<bits/stdc++.h>
#define write printf
#define read scanf
#define endl "\n"
using namespace std;
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	vector<int> vi;
	int num;
	double sum = 0;
	cin >> num;
	for(int i=0; i<num; i++)
	{
		int n ;
		cin >> n;
		vi.push_back(n);
		sum = sum + (n*pow((4.0/5.0),i));
	}
	write("%lf\n",(sum*0.2));
	double ans = 0;
	for(int i=0; i<num; ++i)
	{
		int in = 0;
		double s2=0;
		for(int j=0; j<num; ++j)
		{
			if(j != i)
			{
				s2 += (vi.at(j)*pow((4.0/5.0),in));
				in++;
			}
		}
		ans += (0.2*s2);
	}
	write("%lf",(ans/((double)num)));
}
