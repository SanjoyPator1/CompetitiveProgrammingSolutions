#include <bits/stdc++.h>
using namespace std;


int findNumbers(vector<int>& nums) {

    int sums=0;
    for(int i =0; i<nums.size();i++){
        string str = to_string(nums[i]);
        int len = str.length();
        if(len%2==0){
            sums++;
        }
    }
    
    return sums;
        
}
 
 
// Driver Code
int main()
{
    vector<int> nums =  {12,345,2,6,7896};
    
 
    int ans = findNumbers(nums);
    
    cout<<"Ans: "<<ans<<endl;

}