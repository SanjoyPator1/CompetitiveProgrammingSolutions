#include <iostream>
#include <vector>

using namespace std;

int numIdenticalPairs(vector<int>& nums) {
    int result = 0;
    
    for(int i=0; i<nums.size()-1;i++){
       for(int j=i+1; j<nums.size();j++){
           if(nums[i]==nums[j]){
               result++;
           }
       } 
    }
    
    return result;    
}

int main()
{
    // I/P
    vector<int> vect{ 1,2,3,1,1,3 };
    int ans = numIdenticalPairs(vect);
    cout<<"ans "<<ans;
    
    // O/P = result : 4
    return 0;
}