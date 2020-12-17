/* Soal latihan aritmatika sederhana */

import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.print("Masukkan jumlah kilogram: ");
    int kg = scan.nextInt();
    scan.close();

    int pon = kg * 2;
    int ons = pon * 5;
    int gram = ons * 100;

    System.out.println();
    System.out.print(kg);
    System.out.print("kg sama dengan = ");
    System.out.print(pon);
    System.out.print(" pon atau ");
    System.out.print(ons);
    System.out.print(" ons atau ");
    System.out.print(gram);
    System.out.print(" gram");
  }
}
