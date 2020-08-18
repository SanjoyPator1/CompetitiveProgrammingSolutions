#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

  
// Driver Program to test above function 
int main() 
{
    //take t input
    int t;
    
    
    cin>>t;
    
    //for loop to take input and put it in array
    for(int i =0; i<t; i++){
        int val;
       cin>>val;
       
       for(int i=2; i<=val/i; i++){
            if(val%i==0)
                val=1;
        }

        //display
        if(val == 1)
            cout<<"Not prime"<<endl;
        else
            cout<<"Prime"<<endl;
        
       
       
    }
    
    
    
    return 0; 
} 


