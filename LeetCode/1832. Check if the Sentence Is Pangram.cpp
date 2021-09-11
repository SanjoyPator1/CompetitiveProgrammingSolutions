/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <bits/stdc++.h>

using namespace std;

bool checkIfPangram(string sentence) {

    string allAlpha="abcdefghijklmnopqrstuvwxyz";
    int len = allAlpha.length();
    //cout<<"length of allAlpha "<<len<<endl;
    
    //check with length
    //cout<<"sentence length "<<sentence.length()<<endl;
    if(sentence.length()<len){
        //cout<<"length less"<<endl;
        return false;
    }
    
    vector<bool> present(len,false);
    
    for(int i =0; i<len; i++){
        for(int j = 0; j<sentence.length();j++){
            if(allAlpha[i]==sentence[j]){
                present[i]=true;
            }
        }
    }
    
    bool ans = true;
    
    //cout<<"present vector "<<endl;
    for(auto i: present){
        //cout<<i<<", ";
        if(i==false){
            ans=false;
        }
    }
    
    //cout<<endl;

    return ans;   
}

int main()
{

    
    string sentence = "thequickbrownfoxjumpsoverthelazydog";
    
    bool ans = checkIfPangram(sentence);
    
    cout<<"Ans : "<<ans;

    return 0;
}
