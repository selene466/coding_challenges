// Soal latihan perbandingan sederhana
#include <stdio.h>

int main() {
  int i;
  printf("Input angka: ");
  scanf("%d", &i);
  if (i > 5) {
    printf("%d lebih dari 5", i);
  } else if (i < 5) {
    printf("%d kurang dari 5", i);
  } else {
    printf("%d adalah 5", i);
  }
}
