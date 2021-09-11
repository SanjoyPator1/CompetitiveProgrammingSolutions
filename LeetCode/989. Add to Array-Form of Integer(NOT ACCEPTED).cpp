// NOT ACCEPTED
// For digits greater than 19
// Need to find another solution

#include <bits/stdc++.h>

using namespace std;

 vector<int> addToArrayForm(vector<int>& num, int k) {

    //convert it into string
    string numStr;
    
    for(auto i: num){
        //cout<<"i is "<<i<<endl;
        char temp = '0'+i;
        //cout<<"char is "<<temp<<endl;
        numStr.push_back(temp);
    }
    
    cout<<"numStr is "<<numStr<<endl;
    
    //convert string to single integer - more than 19 digit cant covert
    //int originalNumber = atoi(numStr.c_str());
    unsigned long long int originalNumber;
  	stringstream ( numStr ) >> originalNumber;
	//cout << n;
	
    cout<<"originalNumber in int is "<<originalNumber<<endl;
    
    unsigned long long int ansInt = originalNumber+k;
    
    //convert it back to String
    string ansStr = to_string(ansInt);
    
    //cout<<"ansStr is "<<ansStr<<endl;
    
    //convert it back to vector
    vector<int> ansVec;
    
    for(auto i: ansStr){
        //cout<<"Last loop i is "<<i<<endl;
        //i is in char - convert char to int
        int ia = i - '0';
        //cout<<"Last loop t is "<<ia<<endl;
        ansVec.push_back(ia);
    }
    
    return ansVec;   
}

int main()
{
    vector<int> num = {3,8,0,3,0,2,7,0,7,6,4,9,9,1,7,6,6,1,6};
    
    vector<int> ans = addToArrayForm(num,670);
    
    for(auto i: ans){
        cout<<i<<" ";
    }

    return 0;
}
