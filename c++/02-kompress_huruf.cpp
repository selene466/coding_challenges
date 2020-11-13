// Sebuah lembaga pendidikan akan mengirim kunci jawaban peserta ke kantor pusat pendidikan tersebut.
// Hanya saja mereka menyadari bahwa ternyata filenya terlalu besar oleh karena itu mereka menggunakan penyederhanaan melalui ide kompressi data pada kunci jawaban tersebut.
//
// Aturan kompressi:
// Untuk setiap jawaban yang sama berturut-turut maka hanya akan ditulis satu kali dan angka yang menyatakan perulangan akan ditulis di depannya.
//
// Contoh:
// Input: aaaabbcccdd
// Output: 4a2b3c2d

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void kompresshuruf(string data) {
  string prevhuruf = data.substr(0, 1);
  string dt = data.substr(1);
  int num = 1;
  vector <string> hasil = {};
  for (char& h : dt) {
    string hs(1, h);
    if (hs == prevhuruf) {
      num += 1;
    } else {
      hasil.push_back(to_string(num) + prevhuruf);
      num = 1;
      prevhuruf = hs;
    }
  }
  hasil.push_back(to_string(num) + prevhuruf);
  for (auto hsl : hasil) {
    cout << hsl;
  } // output
}

int main() {
  string data;
  cout << "Input: ";
  cin >> data;
  cout << "Output: ";
  kompresshuruf(data);
}
