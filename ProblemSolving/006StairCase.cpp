#include <bits/stdc++.h>

using namespace std;

void staircase(int n) {
    
    // i = 3, 2, 1, 0 = spaces
    for(int i = n-1 ; i>=0; i--){
         
         //   # = 3 spaces 1 #
         //  ## = 2 spaces 2 #
         // ### = 1 spaces 3 #
         //#### = 0 spaces 4 #
         
        for (int j =1; j<=n; j++){
         if(j<=i){
             cout<<" ";
         }
         else{
             cout<<"#";
         }
        }
        
        cout<<endl;
    }

}

int main()
{
    
    staircase(6);

    return 0;
}
