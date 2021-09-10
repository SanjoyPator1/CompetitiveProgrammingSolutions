#include <bits/stdc++.h>
using namespace std;


 vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies){
    
    vector<bool> ans;
    //find max in original
    int largest=0;
    for(int i=0; i<candies.size();i++){
        largest = max(largest,candies[i]);
    }
    
    //check bool

    for(int j=0; j<candies.size();j++){
        int cs=candies[j]+extraCandies;
        if(cs>=largest){
            ans.push_back(true);
        }
        else{
            ans.push_back(false);
        }
    }
     
    return ans;   
}
 
 
// Driver Code
int main()
{
    vector<int> nums{ 2,3,5,1,3 };
    
 
    vector<bool> ans= kidsWithCandies(nums,3);
    
    for(auto i : ans){
        cout<<i<<" ";
    }
}