// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution
{
    public:
        int findNum(int n)
        {
            int fac = 15625;
            int rem = 3906;
            
            int ans = 0;
            
            while(n > 0)
            {
                if(rem > n) {
                    fac /= 5;
                    rem = (rem - 1) / 5;
                }
                else
                {
                    ans += fac;
                    n -= rem;
                }
            }
            
            return ans;
        }
};

// { Driver Code Starts.


int main() {
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        Solution ob;
        cout <<ob.findNum(n) << endl;
    }
return 0;
}  // } Driver Code Ends