#include <bits/stdc++.h>
using namespace std;


 int numIdenticalPairs(vector<int>& nums){
    
    int ans=0;
    
    for(int i=0; i<nums.size(); i++){
        for(int j = i+1;j<nums.size();j++){
            if(i<j and nums[i]==nums[j]){
                ans++;
            }
        }
    }
     
    return ans;   
}
 
 
// Driver Code
int main()
{
    vector<int> nums{ 1,2,3,1,1,3 };
    
 
    int ans= numIdenticalPairs(nums);
    
    cout<<"ans "<<ans;
}