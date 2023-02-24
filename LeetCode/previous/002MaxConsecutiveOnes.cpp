#include<bits/stdc++.h>
using namespace std;



int findMaxConsecutiveOnes(vector<int>& nums) {
	int p = 0;
	int q = 0;

	for (int i = 0; i < nums.size(); i++) {

		if (nums[i] != 0) {
			q++;
		}
		if (q >= p) {
			p = q;
		}
		if (nums[i] == 0) {
			q = 0;
		}
	}

	return p;


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

	vector<int> vec = {1, 1, 0, 1, 1, 1};

	int res = findMaxConsecutiveOnes(vec);


	cout << "The ans is " << res << endl;



}
