/* Soal latihan membuat kalkulator sederhana */
#include <iostream>
#include <string.h>
#include <math.h> // for sqrt()

using namespace std;

int main() {
  int bil1, bil2, pil;
  float hasil;
  char temp;
  menu:
  cout << "----------\nCalculator\n----------\n\n";
  cout << "Pilih operasi bilangan\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Modulus\n6. Pangkat\n7. Akar\n\nMasukan pilihan: ";
  cin >> pil;
  cout << "\n\n\n";
  switch (pil) {
    case 1:
      cout << "Masukan bilangan 1: ";
      cin >> bil1;
      cout << "Masukan bilangan 2: ";
      cin >> bil2;
      cout << "Hasil: " << bil1 + bil2;
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
    case 2:
      cout << "Masukan bilangan 1: ";
      cin >> bil1;
      cout << "Masukan bilangan 2: ";
      cin >> bil2;
      cout << "Hasil: " << bil1 - bil2;
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
    case 3:
      cout << "Masukan bilangan 1: ";
      cin >> bil1;
      cout << "Masukan bilangan 2: ";
      cin >> bil2;
      cout << "Hasil: " << bil1 * bil2;
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
    case 4:
      cout << "Masukan bilangan 1: ";
      cin >> bil1;
      cout << "Masukan bilangan 2: ";
      cin >> bil2;
      hasil = bil1 / bil2;
      cout << "Hasil: " << hasil;
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
    case 5:
      cout << "Masukan bilangan 1: ";
      cin >> bil1;
      cout << "Masukan bilangan 2: ";
      cin >> bil2;
      hasil = bil1 % bil2;
      cout << "Hasil: " << hasil;
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
    case 6:
      cout << "Masukan bilangan 1: ";
      cin >> bil1;
      cout << "Masukan bilangan 2: ";
      cin >> bil2;
      cout << "Hasil: " << pow(bil1, bil2);
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
    case 7:
      cout << "Masukan bilangan: ";
      cin >> bil1;
      cout << "Hasil: " << sqrt(bil1);
      cout << "\n\nKetik [L] untuk lanjut\n: ";
      cin >> temp;
      goto menu;
      break;
  }
}
