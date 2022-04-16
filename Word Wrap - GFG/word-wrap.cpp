// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++
#include<bits/stdc++.h>
#define vi vector<int>
#define lli long long int
#define inf INT_MAX
lli dp[501];

class Solution {
public:
    lli f(int index, int k, vi &nums, int pre)
    {
        int n = nums.size(); 
        if(index==n) return (-1 * pre);
        if(dp[index]!=-1) return dp[index];
        int prev = 0;
        lli ans = inf;
        for(int i = index; i < n; i++)
        {
            prev += nums[i];
            if(prev > k) break;
            int x = pow(k-prev,2);
            lli temp = x + f(i+1, k, nums, x);
            ans = min(ans, temp);
            prev += 1;
        }
        return dp[index]=ans;
    }

   int solveWordWrap(vi &nums, int k) 
    { 
        memset(dp, -1, sizeof(dp));
        return f(0, k,nums,0);
    } 
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, k;
        cin >> n;
        vector<int>nums(n);
        for (int i = 0; i < n; i++)cin >> nums[i];
        cin >> k;
        Solution obj;
        cout << obj.solveWordWrap(nums, k) << endl;
	}
	return 0;
}  // } Driver Code Ends