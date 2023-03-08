#include <iostream>
#include <vector>

using namespace std;

vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    int maxCandies = 0;
    vector<bool> result(candies.size(),false);
    
    for(int i=0; i<candies.size();i++){
        maxCandies = max(maxCandies,candies[i]);
    }
    
    for(int i=0; i<candies.size();i++){
        if(candies[i]+extraCandies>=maxCandies){
            result[i]=true;
        }
     
        
    }
    
    return result;    
}

int main()
{
    // I/P
    vector<int> vect{ 2,3,5,1,3 };
    int extraCandies = 3;
    vector<bool> result = kidsWithCandies(vect,extraCandies);
    for(auto it : result){
        cout<<it<<endl;
    }
    
    // O/P = result : [true,true,true,false,true] 
    

    return 0;
}