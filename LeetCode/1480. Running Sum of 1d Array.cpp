
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

vector<int> runningSum(vector<int>& nums) {
    int sum = 0;
     for(int i=0; i< nums.size(); i++){
         sum = sum + nums[i];
         nums[i]= sum;
     }
     
     return nums;
        
}


int main()
{
    cout<<"Hello World"<<endl;
    vector<int> vect{ 10, 20, 30 };
    
    
    vector<int>vect1;
    vect1=runningSum(vect);
    for(int i =0; i<vect1.size(); i++){
        cout<<vect1[i]<<endl;
    }

    return 0;
}
