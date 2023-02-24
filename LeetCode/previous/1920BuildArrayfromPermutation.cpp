#include <bits/stdc++.h>
using namespace std;


vector<int> buildArray(vector<int>& nums) {
    
    vector<int> ans(nums.size(),0);    
    for(int i=0; i<nums.size();i++){
        ans[i]=nums[nums[i]];
    }
     
    return ans;   
}
 
 
// Driver Code
int main()
{
    vector<int> nums{ 0,2,1,5,3,4 };

 
    vector<int> ans = buildArray(nums);
    
    for(auto i : ans){
        cout<<i<<" ";
    }
}