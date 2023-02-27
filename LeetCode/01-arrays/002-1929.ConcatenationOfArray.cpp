#include <iostream>
#include <vector>

using namespace std;

vector<int> getConcatenation(vector<int> &nums)
{
    int n = nums.size();

    for (int i = 0; i < n; i++)
    {
        nums.push_back(nums[i]);
    }
    return nums;
}

int main()
{
    // I/P
    vector<int> vect{1, 2, 1};
    vector<int> result = getConcatenation(vect);
    for (auto it : result)
    {
        cout << it << endl;
    }

    // O/P = result : [1,2,1,1,2,1]

    return 0;
}