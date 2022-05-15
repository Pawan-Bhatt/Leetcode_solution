// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
   void solve(vector<int> &arr,vector<vector<int>> &res,vector<int> &temp,int index)
   {
       res.push_back(temp);
       
       for(int i=index;i<arr.size();i++)
       {
           if(i!=index && arr[i]==arr[i-1]) continue;
           
           temp.push_back(arr[i]);
           solve(arr,res,temp,i+1);
           temp.pop_back();
       }
   }

 vector<vector<int> > AllSubsets(vector<int> arr, int n)
   {
       vector<vector<int>> res ;
       vector<int>temp;
       int index = 0;
       sort(arr.begin(),arr.end());
       
       solve(arr,res,temp,index);
       
       return res;
       
   }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> A;
        int x;
        for(int i=0;i<n;i++){
            cin>>x;
            A.push_back(x);
        }
        Solution obj;
        vector<vector<int> > result = obj.AllSubsets(A,n);
        // printing the output
        for(int i=0;i<result.size();i++){
            cout<<'(';
            for(int j=0;j<result[i].size();j++){
                cout<<result[i][j];
                if(j<result[i].size()-1)
                    cout<<" ";
            }
            cout<<")";
        }
        cout<<"\n";
    }
}   


  // } Driver Code Ends