#include <iostream>
#include <vector>

using namespace std;

bool checkIfPangram(string sentence) {
    
    vector<bool> alphabets(26, false); // Create a vector of 26 bools initialized to false

    for (int i = 0; i < sentence.length(); i++) {
        if (sentence[i] >= 'a' && sentence[i] <= 'z') { // Check if the character is an alphabet
            alphabets[sentence[i] - 'a'] = true; // Mark the alphabet as present
        } else if (sentence[i] >= 'A' && sentence[i] <= 'Z') { // Check if the character is an uppercase alphabet
            alphabets[sentence[i] - 'A'] = true; // Mark the alphabet as present
        }
    }


    for (int i = 0; i < 26; i++) {
        if (alphabets[i] == false) { // Check if any alphabet is missing
            return false; // Return false if any alphabet is missing
        }
    }

    return true; // Return true if all alphabets are present

}

int main ()
{
  // I/P
    string sentence = "thequickbrownfoxjumpsoverthelazydog";
    string sentence = "leetcode";

    if (checkIfPangram(sentence)) {
        cout << "The sentence is a Pangram." << endl;
    } else {
        cout << "The sentence is not a Pangram." << endl;
    }
  

  // O/P = result : [2,3,5,4,1,7] 

  return 0;
}