#include <bits/stdc++.h>
using namespace std;


 int diagonalSum(vector<vector<int>>& mat){
    
    int sums =0;
    
    for (int i = 0; i < mat.size(); i++)
    {
        for (int j = 0; j < mat[i].size(); j++)
        {
            //primary sum
            if(i==j){
                sums=sums+mat[i][j];
            }
            
            //secondary sum
            if(i+j==mat.size()-1){
                sums=sums+mat[i][j];
            }
        
        }   

    }
    
    //subtract the extra middle element
    int size=mat.size();
    //cout<<"size is "<<size<<endl;

    if(size%2==0){
        return sums;
    }else{
        int mid= size/2;
        sums= sums-mat[mid][mid];
    }
     
    return sums;   
}
 
 
// Driver Code
int main()
{
    vector<vector<int>> vect = {{1,2,3},{4,5,6},{7,8,9}};
    
    // vector<vector<int>> vect = {{1,1,1,1},
    //           {1,1,1,1},
    //           {1,1,1,1},
    //           {1,1,1,1}};
    
 
    int ans = diagonalSum(vect);
    
    cout<<"Ans: "<<ans<<endl;

}