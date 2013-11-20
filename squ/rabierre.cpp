#include <iostream>
#include <cmath>
using namespace std;
 
long long int gcd(long long int a, long long int b)
{
    long long int c = a % b;
    if(c == 0)
        return b;
 
    return gcd(b, c);
}
 
int main()
{   
    // each w, l input 1 ~ 100,000
    long long int w, l;   cin>>w>>l;
    cout<<w*l/gcd(w,l)/gcd(w,l);
 
    return 0;
}
