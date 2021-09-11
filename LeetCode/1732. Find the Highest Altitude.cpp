#include <bits/stdc++.h>
using namespace std;


 int largestAltitude(vector<int>& gain){
    
    vector<int> alt(gain.size()+1,0);
    
    for(int i=1; i<alt.size();i++){
        alt[i]=alt[i-1]+gain[i-1];
    }
    
    int sum=0;
    
    for(auto i : alt){
        sum = max(sum,i);    
    }
    
    return sum;   
}
 
 
// Driver Code
int main()
{
    vector<int> gain = {-5,1,5,0,-7};
    
 
    int ans= largestAltitude(gain);
    
    cout<<"ANS: "<<ans<<endl;

}