#include<bits/stdc++.h>
using namespace std;



int findNumbers(vector<int>& nums) {

	int e = 0;

	for (int i = 0; i < nums.size() ; i++) {
		int n = 0;
		cout << "checking " << nums[i] << endl;

		while (nums[i] != 0) {
			nums[i] = nums[i] / 10;
			cout << "currently " << nums[i] << endl;
			n++;
			cout << "value of n " << n << endl;
		}

		cout << "value of n " << n << endl;
		if ((n % 2) == 0) {
			cout << "yes even" << endl;
			e++;
		}
	}

	return e;


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

	vector<int> vec = {555, 901, 482, 1771};

	int res = findNumbers(vec);


	cout << "The ans is " << res << endl;



}
