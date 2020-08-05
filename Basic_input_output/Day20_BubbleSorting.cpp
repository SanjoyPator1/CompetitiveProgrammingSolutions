// C++ program for implementation of Bubble sort
#include <bits/stdc++.h>
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

/* Function to print an array */
void print(vector<int> a,int n, int s){
    cout<<"Array is sorted in "<< s <<" swaps."<<endl;
    cout<<"First Element: "<<a[0]<<endl;
    cout<<"Last Element: "<< a[(n-1)]<<endl;
}

// A function to implement bubble sort
void bubbleSort(vector<int> a, int n)
{
    int i, j, swaps=0;
    for (i = 0; i < n-1; i++) {

        // Last i elements are already in place
        for (j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(&a[j], &a[j + 1]);
                swaps++;
            }
        }
    }

    print(a, n , swaps);
}



// Driver code
int main()
{
    //given code-
    int n;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
        cin >> a[a_i];
    }

    bubbleSort(a, n);

    return 0;
}
