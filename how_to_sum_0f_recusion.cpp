#include<bits/stdc++.h>
using namespace std;
template<typename T>
T modulo(T n)
{
  return n == 0?0:n%10+modulo(n/10);
}
