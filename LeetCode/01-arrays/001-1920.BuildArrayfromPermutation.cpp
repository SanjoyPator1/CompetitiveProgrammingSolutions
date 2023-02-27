#include <iostream>
#include <vector>

using namespace std;

vector<int> buildArray(vector<int> &nums)
{
    int n = nums.size();
    // initialize all values with 0
    vector<int> ans(n, 0);

    for (int i = 0; i < n; i++)
    {
        ans[i] = nums[nums[i]];
    }
    return ans;
}

int main()
{
    // I/P
    vector<int> vect{0, 2, 1, 5, 3, 4};
    vector<int> result = buildArray(vect);
    for (auto it : result)
    {
        cout << it << endl;
    }

    // O/P = result : [0,1,2,4,5,3]

    return 0;
}