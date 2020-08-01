#include <iostream>
using namespace std;

#define MAX 100
//for some of the cases I amot checking stack/queue if full/empty for this problem
//I will make another cpp file for stack and queue later
class Solution {
public:
    //Write your code here

    //stack stuff
    char st[MAX];
    char qu[MAX];
    int top =-1;

    //queue stuff
    int front =0,rear =0;



    void pushCharacter(char ch){
        if (top >= (MAX - 1)) {
            cout << "Stack Overflow";
        }
        else {
            st[++top] = ch;
        }
    }

    void enqueueCharacter(char ch){
        qu[rear] = ch;
        rear++;
    }

    char popCharacter(){
        if (top < 0) {
            cout << "Stack Underflow";
            return 0 ;
        }
        else {
            char x = st[top--];
            return x;
        }

    }

    char dequeueCharacter(){
        char y = qu[front++];
        return y;
    }

};

int main() {
    // read the string s.
    string s;
    getline(cin, s);
    
  	// create the Solution class object p.
    Solution obj;
    
    // push/enqueue all the characters of string s to stack.
    for (int i = 0; i < s.length(); i++) {
        obj.pushCharacter(s[i]);
        obj.enqueueCharacter(s[i]);
    }
    
    bool isPalindrome = true;
    
    // pop the top character from stack.
    // dequeue the first character from queue.
    // compare both the characters.
    for (int i = 0; i < s.length() / 2; i++) {
        if (obj.popCharacter() != obj.dequeueCharacter()) {
            isPalindrome = false;
            
            break;
        }
    }
    
    // finally print whether string s is palindrome or not.
    if (isPalindrome) {
        cout << "The word, " << s << ", is a palindrome.";
    } else {
        cout << "The word, " << s << ", is not a palindrome.";
    }
    
    return 0;
}
