
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

vector<int> buildArray(vector<int>& nums) {
    vector<int> vect2;
    for(int i =0; i<nums.size();i++){
        vect2.push_back(nums[i]);
    }
    for(int i =0; i<nums.size();i++){
        vect2.push_back(nums[i]);
    }
    return vect2;    
}


int main()
{
    cout<<"Hello World"<<endl;
    vector<int> vect{ 10, 20, 30 };
    
    
    vector<int>vect1;
    vect1=buildArray(vect);
    for(int i =0; i<vect1.size(); i++){
        cout<<vect1[i]<<endl;
    }

    return 0;
}
