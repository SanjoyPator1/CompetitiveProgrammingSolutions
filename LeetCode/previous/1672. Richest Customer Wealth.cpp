#include <bits/stdc++.h>
using namespace std;


int maximumWealth(vector<vector<int>>& accounts) {
    
    int ms = 0;
    
    for (int i = 0; i < accounts.size(); i++)
    {
        int cs=0;
        for (int j = 0; j < accounts[i].size(); j++)
        {
          cs+=accounts[i][j];  
        }   
        ms= max(ms,cs);
    }
 
    return ms;
}
 
 
// Driver Code
int main()
{
    vector<vector<int>> vect
    {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

 
    int ans = maximumWealth(vect);
    
    cout<<"ans: "<<ans;
}