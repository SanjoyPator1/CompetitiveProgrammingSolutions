#include <bits/stdc++.h>
using namespace std;


 vector<vector<int>> transpose(vector<vector<int>>& matrix)  {

    int m = matrix.size();
    int n = matrix[0].size();
    
    //IMP: mXn  changes to nXm
    vector<vector<int>> ansMatrix(n, vector<int> (m, 0));
    
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size(); j++)
        {
            ansMatrix[j][i]=matrix[i][j];
        }   
    }
 
    return ansMatrix;    
}
 
 
// Driver Code
int main()
{

    
    //vector<vector<int>> vect = {{1,2,3},{4,5,6},{7,8,9}};
    
    vector<vector<int>> vect = {{1,2,3},{4,5,6}};
 
    vector<vector<int>> ans = transpose(vect);
    
    for (int i = 0; i < ans.size(); i++)
    {
        for (int j = 0; j < ans[i].size(); j++)
        {
            cout << ans[i][j] << " ";
        }   
        cout << endl;
    }
 

}