#include <iostream>
#include <climits>

using namespace std;

int main ()
{
  int n, i, j, x;

  cin >> n;
  //ONCE 'for' or 'while', N time repeat.
  for (i =0; i < n; i++) {
    for (j = 0; j < n; j++) x = i+j;
  }

  return 0;

}
int bsearch(int a[], int n, int f)
{
   int left, right, mid;

   left = 0;
   right = n-1;
   while (left <= right) {
     mid = (left+right) / 2;
     if (a[mid] == f) return mid;

     if (a[mid] < f) left = mid+1;
     else right = mid-1;
   }
   return -1;
}
