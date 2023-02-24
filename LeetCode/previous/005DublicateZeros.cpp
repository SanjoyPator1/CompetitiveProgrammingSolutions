/*
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

*/

#include<bits/stdc++.h>
using namespace std;

vector<int> fun(vector<int>& nums) {

	vector<int> res;

	for (int i = 0 ; i < nums.size(); i++) {
		
		if(nums[i]==0){
			//cout<<"if for i= "<<i<<" and nums "<<nums[i]<<endl;

			//copy all the elements one step back
			for (int j = (nums.size()-1) ; j >i; j--){
				//cout<<"for loop - "<<nums[j]<<" and "<<nums[j-1]<<endl;
				nums[j] = nums[j-1];
			}

			// for (int k = 0; k < nums.size(); k++) {
			// 	cout << "The arr now is " << nums[k] << endl;
			// }
			//since it is a 0 jump 1 step for i
			//for total 2 i++ including the for loops i++
			i++;
		}
	}
	res =nums ;

	return res;

}


int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int in, out;
	// cin >> in;

	// out = in * 2;

	// cout << "The output is " << out << endl;

	vector<int> vec = {1,0,2,3,0,4,5,0};

	vector<int> res = fun(vec);

	for (int i = 0; i < res.size(); i++) {
		cout << "The ans is " << res[i] << endl;
	}



}