#include <bits/stdc++.h>

using namespace std;

void miniMaxSum(vector<int> arr) {
    long minSum = 0;
    long maxSum = 0;
    
    
    //we will leave 1  elment everytime
    for(int i =0; i<arr.size(); i ++){
        
        long tempSum =0;
        for(int j = 0; j<arr.size(); j++){
            if(i!=j){
               tempSum = tempSum + arr[j]; 
            }
        }
        
        //cout<<"tempSum is "<<tempSum<<endl;
        
        if(i == 0){
            //cout<<"For 1st value- changed"<<endl;
            minSum = maxSum = tempSum;
        }
        
        if(tempSum<minSum){
            //cout<<"minSum Changed"<<endl;
            minSum = tempSum;
        }
        else if(tempSum > maxSum){
            //cout<<"maxSum Changed"<<endl;
            maxSum = tempSum;
        }
        
        
    }
    cout<<minSum<<" "<<maxSum;

}


int main()
{
    vector<int> arr = {1, 2, 3, 4, 5};
    miniMaxSum(arr);

    return 0;
}
