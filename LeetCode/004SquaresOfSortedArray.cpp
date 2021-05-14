#include<bits/stdc++.h>
using namespace std;



vector<int> sortedSquares(vector<int>& nums) {

	int len = nums.size();

	if (len == 0)
		return nums;

	vector<int> result(len);
	int low = 0, high = len - 1, j = len - 1;
	while (low <= high)
	{
		if (abs(nums[low]) > abs(nums[high]))
		{
			result[j--] = nums[low] * nums[low];
			low++;
		}
		else
		{
			result[j--] = nums[high] * nums[high];
			high--;
		}

	}

	return result;



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

	vector<int> vec = { -7, -3, 2, 3, 11};

	vector<int> res = sortedSquares(vec);

	cout << "The final ans is " << endl;
	for (int i = 0; i < res.size() ; i++) {
		cout << " " << res[i] ;

	}



}
