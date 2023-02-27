#include <iostream>
#include <vector>

using namespace std;

int runningSum(vector<vector<int>> &accounts)
{

    int maxSum = 0;

    for (int i = 0; i < accounts.size(); i++)
    {
        int currentSum = 0;
        for (int j = 0; j < accounts[i].size(); j++)
        {
            currentSum = currentSum + accounts[i][j];
        }
        maxSum = max(maxSum, currentSum);
    }

    return maxSum;
}

int main()
{
    // I/P
    vector<vector<int>> vect{
        {1, 5},
        {7, 3},
        {3, 5}};

    int rows = vect.size();
    int columns = vect[0].size();
    cout << "size of rows = " << rows << " and columns = " << columns << endl;

    int result = runningSum(vect);
    cout << "result " << result << endl;

    // O/P = result :10

    return 0;
}