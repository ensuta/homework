#include <iostream>
#include <climits>
using namespace std;

int main()
{
  int a,max = INT_MIN;

  while (cin >> a) {
    if (a > max) max = a;
  }

  cou << max << endl;

  return 0;
}
