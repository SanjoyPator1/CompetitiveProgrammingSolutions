/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
 
    
    int n;
    
    cin>>n;
    
    int arr[n];
    for(int i=0; i < n ; i++){
        cin>>arr[i];
    
    }
    
    //print
    
    for(int i = (n-1); i>=0; i--){
        cout<<arr[i]<<" ";
    }
    
    
    

    return 0;
}
