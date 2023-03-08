#include <iostream>
#include <vector>

using namespace std;

vector<int> createTargetArray(vector<int>& nums, vector<int>& index){
    
    vector<int> result(nums.size(),0);
    int n = nums.size();
    
    for(int i=0; i<n;i++){
        result.insert(result.begin() + index[i], nums[i]);
    }
    cout<<" n = "<<n<<endl;
    cout<<"result size "<<result.size()<<endl;
    
    // remove elements from position n to position 2n (inclusive)
    result.erase(result.begin() + n, result.end());
    
    return result;   
}

int main()
{
    // I/P
    vector<int> nums{ 0,1,2,3,4 };
    vector<int> index{ 0,1,2,2,1 };
    vector<int> result = createTargetArray(nums,index);
    for(auto it : result){
        cout<<it<<endl;
    }
    
    // O/P = result : [0,4,1,3,2]
    

    return 0;
}