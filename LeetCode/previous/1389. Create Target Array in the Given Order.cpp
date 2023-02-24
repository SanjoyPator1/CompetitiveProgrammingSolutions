#include <bits/stdc++.h>
using namespace std;


 vector<int> createTargetArray(vector<int>& nums, vector<int>& index){
    
    vector<int> a(nums.size(),0);
    vector<int> ans(nums.size(),0);
     
    for(int i=0;i<nums.size();i++){
        a.insert(a.begin() + index[i],nums[i]);
        
    }
    
    // cout<<" a vector : - "<<endl;
    // for(auto i: a){
    //     cout<<i<<", ";
    // }
    // cout<<endl;
    
    for(int i=0;i<nums.size();i++){
        ans[i]=a[i];
        
    }
     
    return ans;   
}
 
 
// Driver Code
int main()
{
    vector<int> nums = {0,1,2,3,4};
    vector<int> index = {0,1,2,2,1};
    
 
    vector<int> ans= createTargetArray(nums,index);
    
    cout<<"ANS: "<<endl;
    for(auto i : ans){
        cout<<i<<", ";
    }
}