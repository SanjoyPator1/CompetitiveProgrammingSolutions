/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    //simple datatypes
    
    int i;
    double d;
    string s;
    
    cin>>i;
    cin>>d;
    
    //to get the whole string including white spaces
    getline(cin >> ws, s); 
    
    double d1=d+4;
    
    cout<<i+4<<endl;
    
    //to get the precision of 1 decimal point of double
    printf("%.1f",d1);
    cout<<endl;
    
    cout<<"Hackerrank "+s;
    return 0;
}
