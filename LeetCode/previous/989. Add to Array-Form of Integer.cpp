

#include <bits/stdc++.h>

using namespace std;

 vector<int> addToArrayForm(vector<int>& num, int k) {

    for(int i = num.size() - 1; i >= 0 && k > 0; --i){
        num[i] += k % 10;
        k/= 10;
        k += num[i]/10;
        num[i] %= 10;
    } 
    while(k){
       num.insert(num.begin(), k % 10);
       k /= 10; 
    } 
    
    return num;  
}

int main()
{
    vector<int> num = {3,8,0,3,0,2,7,0,7,6,4,9,9,1,7,6,6,1,6,4};
    
    vector<int> ans = addToArrayForm(num,670);
    
    for(auto i: ans){
        cout<<i<<" ";
    }

    return 0;
}
