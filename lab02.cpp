#include <iostream>
#include <vector>

using namespace std;

int main() {
    const int x = 3;
    vector<int> le(x);
    vector<int> re(x);
    int temp;

    cout << "Enter the ASCII value of first half of your text: ";
    cin >> le[0];

    cout << "Enter the ASCII value of second half of your text: ";
    cin >> re[0];

    vector<int> key(x - 1);
    
    for (int i = 0; i < x - 1; i++) {
      cout << "Enter " << i + 1 << "th key: ";
      cin >> key[i];
    }

    int ch;
    cout << "Do you want to encrypt or decrypt (1/2): ";
    cin >> ch;

    switch (ch) {
      case 1:  // Encryption
        for (int i = 0; i < x - 1; i++) {
          int function = re[i] ^ key[i];
          re[i + 1] = le[i] ^ function;
          le[i + 1] = re[i];
        }

        temp = re[2];
        re[2] = le[2];
        le[2] = temp;
        break;

      case 2:  // Decryption
        temp = re[2];
        re[2] = le[2];
        le[2] = temp;

        for (int i = x - 2; i >= 0; i--) {
          int function = le[i] ^ key[i];
          le[i + 1] = re[i] ^ function;
          re[i + 1] = le[i];
        }
        break;

    default:
      cout << "Invalid choice!" << endl;
      return 1;
  }
    cout << "le[2]: " << le[2] << " re[2]: " << re[2] << endl;
    return 0;
}
