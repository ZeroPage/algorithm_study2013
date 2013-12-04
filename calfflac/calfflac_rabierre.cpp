#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

#define isAscii(c) (c >= 65 && c <= 90) || (c >= 97 && c <= 122)
    
string longestPalindrome(string text);
string includeEscape(string o, int l, int len);

int main()
{
    string temp, text = "Confucius say: Madam, I'm Adam.";
    stringstream ss;
    while (getline(cin, temp)) {
        if(temp == "")
            break;
        ss<<temp<<"\n";
    }
    
    longestPalindrome(ss.str() == "" ? text : ss.str());
    
    return 0;
}

string expandFromCenter(string s, int c1, int c2)
{
    int l = c1, r = c2;
    while(l >= 0 && r <= s.size()-1 && s[l] == s[r]) {
        --l;
        ++r;
    }

    return s.substr(l+1, r-l-1);
}

string longestPalindrome(string text)
{   
    int n = text.size();
    char c[20001]={'\0'};
    for(int i=0, j=0; i<n; ++i) {
        if(isAscii(text[i]))
            c[j++] = text[i];
    }
    string s(c); transform(s.begin(), s.end(), s.begin(), ::toupper);
    string longestPal;
    int start;

    for(int i=0; i<s.size()-1; ++i) {
        string oddP = expandFromCenter(s, i, i);      // 홀수 palindrome
        if(oddP.size() > longestPal.size()) {
            longestPal = oddP;
            start = i - longestPal.size()/2;
        }

        string evenP = expandFromCenter(s, i, i+1);    // 짝수 palindrome
        if(evenP.size() > longestPal.size()) {
            longestPal = evenP;
            start = i - longestPal.size()/2+1;
        }
    }

    cout<<longestPal.size()<<endl;
    cout<<includeEscape(text, start, longestPal.size())<<endl;
    
    return longestPal;
}

string includeEscape(string o, int l, int len)
{
    char result[2001] = {'\0'};
    for(int i=0, j=0, cnt=-1; i<o.size(); ++i) {
        if(isAscii(o[i]))
            cnt++;
        if(l <= cnt)
            result[j++] = o[i];
        if(len == cnt - l + 1)
            break;
    }
    return result;
}