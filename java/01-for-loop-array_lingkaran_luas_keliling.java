/*
Soal:
Buatlah program untuk menghitung luas dan keliling sejumlah (lebih dari 1) lingkaran, dimana jumlah lingkaran dan nilai jari-jari dari masing-masing lingkaran diinput oleh user
*/

import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner jml_inp = new Scanner(System.in);
    System.out.print("Jumlah lingkaran: ");
    int jml = jml_inp.nextInt();

    int lingkaran[] = new int[jml];

    for (int i = 0; i < jml; i++) {
      Scanner lingkaran_inp = new Scanner(System.in);
      System.out.print("Jari-jari lingkaran ke ");
      System.out.print(i + 1);
      System.out.print(": ");
      int lingkaranper = lingkaran_inp.nextInt();

      lingkaran[i] = lingkaranper;
    }

    System.out.println("==========");

    for (int i = 0; i < jml; i++) {
      int jari = lingkaran[i];
      float luas = 3.14f * jari * jari;
      float keliling = 2f * 3.14f * jari;

      System.out.print("Lingkaran ke ");
      System.out.println(i + 1);
      System.out.print("Jari-jari: ");
      System.out.println(jari);
      System.out.print("Luas: ");
      System.out.println(luas);
      System.out.print("Keliling: ");
      System.out.println(keliling);

      System.out.println("-----");
    }
  }
}
