/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream> 
using namespace std; 
  
// function to convert decimal to binary 
void decToBinary(int n) 
{ 
    // array to store binary number 
    int binaryNum1[32], binaryNum2[32]; 
  
    // counter for binary array 
    int i = 0; 
    while (n > 0) { 
  
        // storing remainder in binary array 
        binaryNum1[i] = n % 2; 
        n = n / 2; 
        i++; 
    } 
  
    int k=0; 
    for (int j = i - 1; j >= 0; j--){ 
        binaryNum2[k] = binaryNum1[j];
        k++;
    }
        
    // printing binary array
    for (int j = 0; j <i; j++){ 
        cout<<binaryNum2[j];
    }
    
    int sum =0;
    if(binaryNum2[0]==0){
        for(int j =1; j<i; j++){
            if(binaryNum2[j]!=0){
                sum++;
            }
            else
                break;
        
        }
    }
    else
    {
        for(int j =0; j<i; j++){
            if(binaryNum2[j]!=0){
                sum++;
            }
            else
                break;
        }
        
    }
    
    //final ans print
    cout<<endl<<"consecutive 1's are - "<<sum;
    
} 
  
// Driver program to test above function 
int main() 
{ 
    int n;
    cin>>n;
    
    decToBinary(n); 
    return 0; 
}
