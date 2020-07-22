/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int n,d;
    
    cin>>n>>d;
    
    int arr[n];
    
    for(int i=0; i<n ; i++){
        cin>>arr[i];
    }
    
    //store d elements in temp_arr
    
    int temp_arr[d];
    
    for(int j =0; j<d; j++){
        temp_arr[j] = arr[j];
    }
    
    //display temp_arr 
    cout<<"displaying temp_arr : - "<<endl;
    for(int q=0; q<d ; q++){
        cout<<temp_arr[q]<<" ";
    }
    
    cout<<endl;
    
    //shift rest of the elements of the arr to left
    int a = d;
    for(int k =0; k <(n-d) ; k++){
        arr[k] = arr[a];
        a++;
    }
    
    //display arr after shifting
    cout<<"displaying arr after shifting : - "<<endl;
    for(int q=0; q<n ; q++){
        cout<<arr[q]<<" ";
    }
    
    cout<<endl;
    
    //store back the d elemenst
    int b=0;
    for(int p=(n-d); p<n; p++){
        arr[p]= temp_arr[b];
        b++;
    }
    
    //final display
    cout<<"final ans: - "<<endl;
    for(int q=0; q<n ; q++){
        cout<<arr[q]<<" ";
    }
    
    
    return 0;
}
