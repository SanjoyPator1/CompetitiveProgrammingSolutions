#include <bits/stdc++.h>
using namespace std;


 int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue){
    
    int keyCol=0;
    if(ruleKey=="type"){
        keyCol=0;
    }else if(ruleKey=="color"){
        keyCol=1;
    }else{
        keyCol=2;
    }
    
    int sum=0;
     
    for (int i = 0; i < items.size(); i++)
    {
        if(items[i][keyCol]==ruleValue){
            sum++;
        }
    }
     
    return sum;   
}
 
 
// Driver Code
int main()
{
    vector<vector<string>> items = {
        {"phone","blue","pixel"},{"computer","silver","lenovo"},{"phone","gold","iphone"}};
    
 
    int ans= countMatches(items,"color","silver");
    
    cout<<"ANS: "<<ans<<endl;

}