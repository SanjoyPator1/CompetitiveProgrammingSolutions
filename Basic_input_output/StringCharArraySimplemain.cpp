#include <bits/stdc++.h>

using namespace std;

int main() 
{ 
     //this is the simplest way- as strings can be treated as array of characters
     //another way is there to use the function
        // assigning value to string s 
        string s ;
        int n;
        
        //to get string input along with white spaces
        getline(cin >> ws, s);
        
        n = s.length(); 
        
        // declaring character array 
        char char_array[n + 1]; 
        
        // copying the contents of the 
        // string to char array 
        
        
        //set
        for(int j =0 ; j<n; j++){
            char_array[j]=s[j];
        }
        
        //print
        for(int j =0 ; j<n; j++){
            cout<<char_array[j];
        }
        
    
    
  
    return 0; 
} 