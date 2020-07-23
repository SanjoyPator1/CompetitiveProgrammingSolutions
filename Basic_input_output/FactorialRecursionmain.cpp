/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int factorial(int n){
    
    if(n>1){
        //cout<<"value of n is-  "<<n<<endl;
        
        
        return n*factorial(n-1);
    }
    return 1;
    
}

int main()
{
    int n;
    
    cin>>n;
    
    int result = factorial(n);
    cout<<result;
    

    return 0;
}
