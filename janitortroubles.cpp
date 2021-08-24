#include<bits/stdc++.h>
using namespace std;
template<typename... T>
void read(T&... args)
{
	((cin>>args),...);
}
int main(void)
{
	int s1,s2,s3,s4;
	read(s1,s2,s3,s4);
	double ms = (s1+s2+s3+s4)/2.0;
	printf("%.6f",sqrt((ms-s1)*(ms-s2)*(ms-s3)*(ms-s4)));
	return 0;
}
