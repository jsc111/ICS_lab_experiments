#include<iostream>
#include<string>

using namespace std;

string encrypt(string text, int shift){
  string result = "";

  for(char c : text){
    if (isalpha(c)){
      int pos = c - 'a';
      pos = (pos + shift + 26) % 26;
      result += 'a' + pos;
    } else {
      result += c;
    }
  }
  return result;
}

int main(){
    int t, ch;
    cout << "Enter number of test cases: ";
    cin >> t;
    cin.ignore();

    string text, encrypted, decrypted;
    int shift;
    
    while(t){
      cout << "Do you want to ENCRYPT or DECRYPT (1/2): ";
      cin >> ch;
      cin.ignore(); 

      cout << "Enter the text to be worked on: ";
      getline(cin, text);

      cout << "Enter the shift key: ";
      cin >> shift;
      cin.ignore(); 

      if(ch == 1){
          encrypted = encrypt(text, shift);
          cout << "Encrypted Text: " << encrypted << endl; 
      }

      if(ch == 2){
          decrypted = encrypt(text, (-shift)%26);
          cout << "Decrypted Text: " << decrypted << endl; 
      }

      t--;
    }

    return 0;
}
