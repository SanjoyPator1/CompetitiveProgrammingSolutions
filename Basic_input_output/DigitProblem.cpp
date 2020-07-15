/*
// Sample code to perform I/O:

cin >> name;                            // Reading input from STDIN
cout << "Hi, " << name << ".\n";        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here

#include<iostream>

using namespace std;

int main(){

    unsigned long long x;
	int y;
	cin >> x >> y;

	//cout << x << " " << y;

	string s;

	s = to_string(x);
	int s_len = s.length();

	//cout << s << " " << s_len;

	unsigned long long arr[s_len];

	//putting integers in the array
	for (int i = (s_len - 1); i >= 0; i--) {
		arr[i] = x % 10;	//putting the remainder into the array
		x /= 10;	//decreasing an unit from the last - i.e taking the quotient

	}

	//changing the first y number to 9
	for (int j = 0; j < y; j++) {
		arr[j] = 9;
	}

	//putting each digit of array into a single integer - result
	unsigned long long result = 0;
	for ( int temp = 0; temp < s_len; temp++) {
		result *= 10;
		result += arr[temp];
	}

	cout << result;


    return 0;
}
