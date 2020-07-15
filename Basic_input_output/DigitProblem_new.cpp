#include<bits/stdc++.h>

using namespace std;

int main(){

             string x;

             int k;

             cin>>x>>k;

             for(int i=0;i<x.size();i++){ 

                  if(x[i]!='9'){

                      if(k){	//after k no. of times - k becomes 0(false) - go out of loop 
                       x[i]='9';
                        k--;	//everytime k decreases by 1
                        }

                   }

           }

             cout<<x<<endl;

}
