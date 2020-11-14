// Soal:
//  Buat array 2 dimensi dengan bentuk secara otomatis
//  Jika dientri data melalui keyboard untuk ukuran matrik misal 4 atau 5 atau 6 dst
//  Maka bentuk matrik otomatis seperti berikut:
//
//  1001           10001        100001
//  1101           11001        110001
//  1011           10101        101001
//  1001           10011        100101
//                 10001        100011
//                              100001
//  input = 4     input = 5     input = 6

#include <iostream>
#include <string>

using namespace std;

int main() {
  int inp;
  int baris = 0;
  int kolom = 0;
  cout << "Input: ";
  cin >> inp;
  int mtrx[inp][inp];
  for (int i = 0; i < inp; ++i) {
    kolom = 0;
    for (int j = 0; j < inp; ++j ) {
      if (j == 0) {
        mtrx[baris][kolom] = 1;
        ++kolom;
      } else if (j == (inp - 1)) {
        mtrx[baris][kolom] = 1;
        ++kolom;
      } else {
        if (j == baris) {
        mtrx[baris][kolom] = 1;
        ++kolom;
        } else {
        mtrx[baris][kolom] = 0;
        ++kolom;
        }
      }
    }
    ++baris;
  }
  for (int x = 0; x < inp; ++x) { // output
    for (int z = 0; z < inp; ++z) {
      cout << mtrx[x][z];
    }
    cout << endl;
  }
}
