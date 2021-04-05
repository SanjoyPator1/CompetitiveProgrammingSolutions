/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

//function
void plusMinus(vector<int> arr) {
    
    double n = arr.size();
    int pSum = 0;
    int nSum = 0;
    int zSum = 0;
     
     for (int i = 0; i <n ; i++){
         int element = arr[i];
         //cout<<"The element is "<<element<<endl;
         
         //conditions
         if(element>0){
             pSum++;
         }
         else if(element<0){
             nSum++;
         }
         else{
             zSum++;
         }
         
     }
     
    //  cout<<"psum is "<<pSum<<endl;
    //  cout<<"nsum is "<<nSum<<endl;
    //  cout<<"zsum is "<<zSum<<endl;
     
     
     //proportions
    double pProp = pSum / n;
    double nProp = nSum / n;
    double zProp = zSum / n;
         
         
    cout << fixed << setprecision(6) << pProp <<endl;
    cout << fixed << setprecision(6) << nProp <<endl;
    cout << fixed << setprecision(6) << zProp <<endl;
     
}

int main()
{
    cout<<"Hello World"<<endl;;
    vector<int> arr = {-4, 3, -9, 0, 4, 1};
    
    plusMinus(arr);

    return 0;
}
