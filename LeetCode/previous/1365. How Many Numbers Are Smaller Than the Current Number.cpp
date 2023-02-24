#include <bits/stdc++.h>
using namespace std;


 vector<int> smallerNumbersThanCurrent(vector<int>& nums){
    
    vector<int> ans(nums.size(),0);
     
    for(int i=0;i<nums.size();i++){
        
        for(int j =0; j<nums.size(); j++){
            if(i!=j and nums[j]<nums[i]){
                ans[i]++;
            }
        }
    }
     
    return ans;   
}
 
 
// Driver Code
int main()
{
    vector<int> nums{ 8,1,2,2,3 };
    
 
    vector<int> ans= smallerNumbersThanCurrent(nums);
    
    for(auto i : ans){
        cout<<i<<" ";
    }
}