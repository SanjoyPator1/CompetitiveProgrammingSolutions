#include <iostream>
#include <vector>

using namespace std;

vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    
    vector<int> result(nums.size(),0);
    
    for(int i=0; i<nums.size();i++){
        int count =0;
       for(int j=0; j<nums.size();j++){
           if(i!=j && (nums[j]<nums[i])){
               count++;
           }
       }
       result[i] = count;
    }
    
    return result;   
}

int main()
{
    // I/P
    vector<int> vect{ 8,1,2,2,3 };
    vector<int> result = smallerNumbersThanCurrent(vect);
    for(auto it : result){
        cout<<it<<endl;
    }
    
    // O/P = result : [4,0,1,1,3]
    

    return 0;
}