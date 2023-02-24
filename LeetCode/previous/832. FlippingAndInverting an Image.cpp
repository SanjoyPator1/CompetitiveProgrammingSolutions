#include <bits/stdc++.h>
using namespace std;


 vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image){
    
    int rowSize = image.size();
    int colSize = image[0].size();
    
    //cout<<"Row Size : "<<rowSize<<" & Col Size : "<<colSize<<endl;
    
    //horizontal flip
    for (int i = 0; i < rowSize; i++)
    {
        int s=0, e =image[i].size()-1;
        
        while(s<e){
            //cout<<"For s = "<<s<<" & e= "<<e<<endl;
            int a =image[i][s];
            image[i][s] = image[i][e];
            image[i][e] = a;
            s++;
            e--;
        }
    }
    
    
    // //Invert Image i.e conver 0 to 1 and 1 to 0
    for (int i = 0; i < image.size(); i++)
    {
        for (int j = 0; j < image[i].size(); j++)
        {
            if(image[i][j]==0){
              image[i][j]=1;  
            }else{
              image[i][j]=0; 
            }
        }   

    }
    
    
     
    return image;   
}
 
 
// Driver Code
int main()
{
    vector<vector<int>> image = {{1,1,0},{1,0,1},{0,0,0}};
    
 
    vector<vector<int>> ans= flipAndInvertImage(image);
    
    for (int i = 0; i < ans.size(); i++)
    {
        for (int j = 0; j < ans[i].size(); j++)
        {
            cout << ans[i][j] << " ";
        }   
        cout << endl;
    }

}