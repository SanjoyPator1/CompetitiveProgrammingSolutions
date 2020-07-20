#include <bits/stdc++.h>

using namespace std;

int main() 
{ 
     
    //t is the number of test cases
    // n is the length of string
    int t,n ;
 
    cin>>t;
  
    for (int i = 0; i < t; i++){
        
        
        // assigning value to string s 
        string s ;
        
        //to get string input along with white spaces
        getline(cin >> ws, s);
        
        n = s.length(); 
        
        // declaring character array 
        char char_array[n + 1]; 
        
        // copying the contents of the 
        // string to char array 
        strcpy(char_array, s.c_str());
        
        //print even
        for(int j =0 ; j<n; j=j+2){
            cout<<char_array[j];
        }
        
        
        cout<<" ";
        //print odd
        for(int k =1 ; k<n; k=k+2){
            cout<<char_array[k];
        }
        
        cout<<endl;
        
    }
        
    
  
    return 0; 
} 