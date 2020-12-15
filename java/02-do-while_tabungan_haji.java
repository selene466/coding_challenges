/*
Soal:
1. Seorang mau menabung untuk pembiayaan ibadah hajinya.
Biaya ibadah haji saat ini senilai `a` juta.
Jika tiap bulan dia mampu menabung sebesar `b` rupiah.
Dengan program anda yang menggunakan fungsi, bantulah orang ini untuk menghitung berapa bulan dia butuhkan agar biaya hajinya bisa terpenuhi.

Yang menjadikan masalah ini tidak dapat diselesaikan dengan pembagian langsung `a / b` adalah bahwa setiap tahun biaya haji naik rata-rata `c%` dari biaya awal `a`.

Nilai a, b, c dimasukkan oleh user.


2. Jika nilai `c` adalah kenaikan dari tahun sebelumnya dan setiap 6 bulan sekali dia mendapatkan bonus gaji sebesar `d` ribu yang selalu dia gunakan untuk menambah tabungan hajinya, berapa bulan dia butuhkan agar biaya hajinya terpenuhi?


Buatlah implementasi dalam bahasa pemrograman JAVA.
*/

import java.util.*;

class Main {
  static int hitungBulan(float biayaSaatIni, float gajiBulanan, float kenaikanTahun) {
    int bulan = 0;
    float d = 200.000f;
    float totalGaji = 0.0f;

    do {
      if ((bulan % 12) == 0) {
        biayaSaatIni += (biayaSaatIni * (kenaikanTahun / 100.0f));
      }

      if ((bulan % 6) == 0) {
        totalGaji += d;
      }

      totalGaji += gajiBulanan;
      bulan++;
      if (bulan >= 1008) {
        System.out.println("Lebih dari 1008 bulan / 84 tahun");
        System.exit(0);
      }
    } while (totalGaji < biayaSaatIni);

    return bulan;
  }

  public static void main(String[] args) {
    Scanner biaya_inp = new Scanner(System.in);
    System.out.print("Biaya haji saat ini\t: ");
    float a = biaya_inp.nextFloat();

    Scanner gaji_inp = new Scanner(System.in);
    System.out.print("Gaji bulanan\t\t: ");
    float b = gaji_inp.nextFloat();

    Scanner kenaikan_inp = new Scanner(System.in);
    System.out.print("Kenaikan % per tahun\t: ");
    float c = kenaikan_inp.nextFloat();

    biaya_inp.close();

    System.out.println();
    System.out.print("Bulan yg dibutuhkan: ");
    System.out.println(hitungBulan(a, b, c));
  }
}
