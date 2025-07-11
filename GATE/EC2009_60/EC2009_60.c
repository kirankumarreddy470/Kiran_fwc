#include <stdio.h>

int main() {
    printf("Q60. What are the minimum numbers of NOT gates and 2-input OR gates required to design the logic of the driver for this 7-segment display?\n\n");

    printf("(A) 3 NOT and 4 OR\n");
    printf("(B) 2 NOT and 4 OR\n");
    printf("(C) 1 NOT and 3 OR\n");
    printf("(D) 2 NOT and 3 OR\n\n");

    printf("Correct Answer: (A) 3 NOT and 4 OR\n\n");

    printf("Solution:\n");
    printf("A 7-segment display driver converts a 4-bit BCD input (0-9) to signals controlling segments a-g.\n");
    printf("Each segment requires its own logic equation involving the inputs and their inverses.\n\n");

    printf("Key points:\n");
    printf("1. The minimum number of NOT gates is 3, needed to generate the necessary inverted inputs (like ~A, ~B).\n");
    printf("2. The minimum number of 2-input OR gates is 4, required to combine product terms for the segment logic.\n\n");

    printf("Therefore, after minimizing the logic for all segments, the optimal solution uses 3 NOT gates and 4 OR gates.\n");

    return 0;
}

