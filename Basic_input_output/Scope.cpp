#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Difference {
private:
    vector<int> elements;

public:
    int maximumDifference;

    // Add your code here
    //constructor
    Difference(vector<int> e){
        this->elements = e;

    }
    //method
    void computeDifference() {
        maximumDifference = 0;

        for (int i = 0; i < (elements.size() - 1); i++) {
            for (int j = (i + 1); j < elements.size(); j++) {
                int t = abs(elements[i] - elements[j]);

                if (t >= maximumDifference) {
                    maximumDifference = t;

                }
            }

        }
    }

}; // End of Difference class

int main() {
    int N;
    cin >> N;

    vector<int> a;

    for (int i = 0; i < N; i++) {
        int e;
        cin >> e;

        a.push_back(e);
    }

    Difference d(a);

    d.computeDifference();

    cout << d.maximumDifference;

    return 0;
}
