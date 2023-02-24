#include<bits/stdc++.h>
using namespace std;

//Move all negative numbers to beginning and positive to end with constant extra space

vector<int> twoSum(vector<int>& nums, int target) {

	vector<int> res;

	for (int i = 0 ; i < nums.size(); i++) {
		for (int j = i + 1; j < nums.size(); j++) {

			int ans = nums[i] + nums[j];

			if (ans == target) {
				res = {i, j};
				return res;

			}
		}
	}
	res = {0, 0};

	return res;

}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int in, out;
	cin >> in;

	out = in * 2;

	cout << "The output is " << out << endl;

	vector<int> vec = {3, 2, 4};

	vector<int> res = twoSum(vec, 6);

	for (int i = 0; i < res.size(); i++) {
		cout << "The ans is " << res[i] << endl;
	}


}
