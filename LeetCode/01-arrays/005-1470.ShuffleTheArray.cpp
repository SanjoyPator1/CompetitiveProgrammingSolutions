#include <iostream>
#include <vector>

using namespace std;

vector<int> shuffle(vector<int> &nums, int n)
{
    cout << "n = " << n << endl;
    vector<int> vect(nums.size(), 0);

    // example
    // i/p ind=[0,1,2,3,4,5]
    //  i/p = [1,2,3,10,20,30]
    // o/p ind=[0,3,1, 4, 2, 5]
    //  o/p = [1,10,2,20,3,30]
    int count = 0;
    for (int i = 0; i < n * 2; i = i + 2)
    {
        cout << "i = " << i << " cout=" << count << endl;
        vect[i] = nums[count];
        vect[i + 1] = nums[count + n];
        count++;
    }

    return vect;
}

int main()
{
    // I/P
    vector<int> vect{2, 5, 1, 3, 4, 7};

    vector<int> result = shuffle(vect, vect.size() / 2);

    cout << "Result : ";
    for (int i = 0; i < result.size(); i++)
    {

        cout << result[i] << " ";
    }

    // O/P = result : [2,3,5,4,1,7]

    return 0;
}