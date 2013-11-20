#include <iostream>
#include <cmath>
using namespace std;
 
int main()
{
   int i,n;
 
   scanf("%d",&n);
 
   for(i = 2 ; i <= sqrt((double)n) ; ++i){
      if ( n % i == 0 ) break;
   }
   if(i > sqrt((double)n))   
       i = n;
   cout<<n-(n/i);
}
