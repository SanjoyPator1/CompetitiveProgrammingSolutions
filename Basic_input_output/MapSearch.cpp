
#include <bits/stdc++.h> 
using namespace std; 

int main()
{
    int n;
    cin>>n;
    
    //take input
    map<string, string> mpp;
    
    for(int i=0; i<n; i++){
        string name, ph;
        cin>>name>>ph;
        
        mpp.insert({name, ph});
    }
    
    //search
    //find() returns a pointer to end() if key is not found
    
    string  search;
    while(cin>>search){
    
    auto it = mpp.find(search); 
      
    if(it == mpp.end()) 
        cout << "Not found" <<endl; 
    else
        cout<< it->first << "=" << it->second <<endl; 
    }
        
    return 0;
}
