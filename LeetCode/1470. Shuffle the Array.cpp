#include <bits/stdc++.h>
using namespace std;


 vector<int> shuffle(vector<int>& nums, int n){
    
    vector<int> ans(nums.size(),0);
    
    //1st loop
    int a=0;
    for(int i=0; i<n;i++){
        ans[a]= nums[i];
        a=a+2;
    }
    
    //2nd loop
    int b=1;
    for(int j=n; j<2*n;j++){
        ans[b]= nums[j];
        b=b+2;
    }
     
    return ans;   
}
 
 
// Driver Code
int main()
{
    vector<int> nums{ 2,5,1,3,4,7 };
    
    int n = nums.size()/2;
 
    vector<int> ans = shuffle(nums,n);
    
    for(auto i : ans){
        cout<<i<<" ";
    }
}