#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	float N,K_judges,sum=0;
	cin >> N >> K_judges;
	float min = 0, max = 0;
	for(int i=0; i<K_judges; i++){
		int rate;
		cin>>rate;
		sum = sum + rate;
	}
	if(N == K_judges) cout << sum/N << " " << sum/N << "\n";
	else{
	int remaining = N - K_judges;
	min = (float(sum) + (remaining*-3))/ N ;
	max = (float(sum) + (remaining*3))/ N;
	cout <<  min << " " << max << "\n";
}
	return 0;
}