#include<bits/stdc++.h>
#define write printf 
#define _for_(a,b) for(int i=a; i<=b; i++)
#define _inFor_(a,b) for(int j=a; j<=b; j++)
using namespace std;
template<typename... T>
void read(T&... args)
{
	((cin>>args),...);
}
int main(void)
{
	int value;
	read(value);
	int mid_value = (value/2)+1;
	cout <<value<<":"<<"\n";
	_for_(2,mid_value)// for appealing reasons it should not be same! so starting from 2
	{
		_inFor_(i-1,i)
		{
			int loop = 1;
			int max = 0;
			while(true)
			{
			 int sum = (i * loop)+(j*loop);//checking and initializing the sum here
			 if(sum > value)
			 {
			 	break;
			 }
			 if(sum > max)
			 {
			 	max = sum;
			 }
			 loop = loop + 1;
			}
			if(max < value && (value-max) == i)//the difference should be same as the ith value if it is not same as the difference should be the bigger one.:)
			{
				cout << i <<","<< j << endl;
			}
			if(max == value)
			{
				cout << i <<","<< j << endl;
			}
		}
	}
}
