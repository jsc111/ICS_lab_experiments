#include<iostream>
#include<algorithm>
#include<cctype>
#include<cmath>

using namespace std;

int main(){
  int p,q;
  cout<<"Enter 2 prime nos as p and q: ";
  cin>>p>>q;

  int n = p*q;
  cout<<"\nValue of n:"<<n;
  int totN = (p-1)*(q-1);
  cout<<"\nValue of totn:"<<totN;

  int e;
  for (int i = 2; i < totN; i++){
    if (__gcd(i,totN) == 1){
      e = i;
      cout<<"\nThis is e: "<<e;
      break;
    }
  }
  int d;
  for (int k = 0; ; k++){
    if ((1 + (k * totN)) % e == 0){
      d = (1 + (k * totN)) / e;
      cout << "\nValue of K: " << k;
      break;
    }
  }
  cout<<"\nValue of d: "<<d;

  int M;
  cout<<"\nEnter plain text to encrypt (<"<<n<<"): ";
  cin>>M;

  int expo = pow(M,e);
  int c = expo%n;
  cout<<"\nAfter Encryption: "<<c;

  int expoM= pow(c,d);
  int message = expoM%n;
  cout<<"\nAfter Decryption: "<<message;
  return 0;
}
