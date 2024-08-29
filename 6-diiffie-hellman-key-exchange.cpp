#include <iostream>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

long long mod_exp(long long base, long long exp, long long mod){
  long long result = 1;
  while (exp > 0){
    if (exp % 2 == 1){ 
      result = (result * base) % mod;
    }
    exp = exp >> 1; 
    base = (base * base) % mod;
  }
  return result;
}

int is_prime(int p){
  if (p <= 1)
    return 0;
  for(int i = 2; i <= sqrt(p); ++i) {
    if (p % i == 0) 
      return 0; 
  }
  return 1;
}

vector<int> findPrimitiveRoots(int p){
    vector<int> primitiveRoots;
    int totn = p - 1;
    
    
    vector<int> factors;
    for (int i = 1; i * i <= totn; ++i){
      if (totn % i == 0) {
        factors.push_back(i);
        if (i != totn / i)
          factors.push_back(totn / i);
      }
    }
    
    for (int g = 2; g < p; ++g) {
      bool isPrimitiveRoot = true;
      for (int factor : factors) {
        if (mod_exp(g, factor, p) == 1 && factor != totn) {
          isPrimitiveRoot = false;
          break;
        }
      }
      if (isPrimitiveRoot)
        primitiveRoots.push_back(g);
    }
    
    return primitiveRoots;
}

int main() {
    
    // Taking initial prime nos
    int p;
    cout << "Enter a prime number (p): ";
    cin >> p;
    while (is_prime(p) != 1){
      cout << "Invalid prime number. Please enter a prime number: ";
      cin>> p;
    }
    
    // Find all primitive roots of p
    vector<int> primitiveRoots = findPrimitiveRoots(p);
    cout << "Primitive roots of " << p << " are: ";
    for (int root : primitiveRoots) {
        cout << root << " ";
    }
    cout << endl;

    // Asking for the user's choice of primitive root
    int g;
    cout << "Enter a primitive root of your prime number (g): ";
    cin >> g;

    // Based on p asking for private keys
    int a_pk, b_pk;

    cout << "Alice may enter a private key (< p): ";
    cin >> a_pk;
    cout << "Bob may enter a private key (< p): ";
    cin >> b_pk;

    // Based on private keys generate public keys
    long long A_pb = mod_exp(g, a_pk, p);  
    long long B_pb = mod_exp(g, b_pk, p);  

    // Sharing of public keys of both users
    cout << "Public keys exchanged:" << endl;
    cout << "Alice's public key (A): " << A_pb << endl;
    cout << "Bob's public key (B): " << B_pb << endl;

    // Checking if the shared key is valid with both users
    long long sharedSecretA = mod_exp(B_pb, a_pk, p);  
    long long sharedSecretB = mod_exp(A_pb, b_pk, p);  

    cout << "\nShared secret keys calculated:" << endl;
    cout << "Alice's shared secret: " << sharedSecretA << endl;
    cout << "Bob's shared secret: " << sharedSecretB << endl;

    if (sharedSecretA == sharedSecretB) {
        cout << "\nThe shared secret is successfully established!" << endl;
    } else {
        cout << "\nError: The shared secrets do not match!" << endl;
    }

    return 0;
}
