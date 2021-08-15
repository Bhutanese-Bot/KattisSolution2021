#include<bits/stdc++.h>
using namespace std;
long long modulo(long long n);
long long modulo(long long n){
	long long sum;
	while(n != 0){
		long long rem = n % 10;
		sum += rem;
		n = n / 10;
	}
	return sum;
}
int main()
{
	long long loop;
	cin >> loop;
	cout << modulo(20) << endl;
//	for(long long i=1; i<=loop; i++){
//		long long num;
//		long long ans = 0;
//		cin >> num;
//		for(long long j=0; j<=num; ++j){
//			long long sum_of_N;
//			sum_of_N = modulo(num);
//			cout << modulo(j) << endl;
//			if(modulo(j) < sum_of_N && (sum_of_N-modulo(j) == 1)){
//				ans = j;
//			}
//		}
//		cout << ans << endl;	
//	} 
}
