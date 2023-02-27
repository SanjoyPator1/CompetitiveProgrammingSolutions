#include <iostream>
#include <vector>

using namespace std;

vector<int> runningSum(vector<int> &nums)
{

    int n = nums.size();

    int prevSum = 0;

    for (int i = 0; i < n; i++)
    {
        nums[i] = nums[i] + prevSum;
        prevSum = nums[i];
    }
    return nums;
}

int main()
{
    // I/P
    vector<int> vect{1, 2, 3, 4};
    vector<int> result = runningSum(vect);
    for (auto it : result)
    {
        cout << it << endl;
    }

    // O/P = result : [1,3,6,10]

    return 0;
}