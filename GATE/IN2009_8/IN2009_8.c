#include <stdio.h>

int main() {
    printf("Q8. The minimal sum-of-products expression for the logic function f represented by the given Karnaugh map is:\n\n");

    printf("(A) QS + P'R'S + P'RS' + PQR'\n");
    printf("(B) QS + P'R'S + P'RS + PQR\n");
    printf("(C) P'RS + P'QR' + P'RS' + PQR\n");
    printf("(D) P'R'S + PQR + P'RS + PQR'\n\n");

    printf("Correct Answer: (D) P'R'S + PQR + P'RS + PQR'\n\n");

    printf("Explanation:\n");
    printf("1. The Karnaugh map shows where f=1; grouping adjacent 1s minimizes the expression.\n");
    printf("2. The groups formed are:\n");
    printf("   - QS: covers multiple 1s in PQ=01 rows.\n");
    printf("   - PQR: a specific cell at PQ=11, RS=01.\n");
    printf("   - P'QR': covers PQ=10, RS=01.\n");
    printf("   - P'R'S: covers PQ=00, RS=11.\n");
    printf("3. These minimal terms match exactly with option D.\n");

    return 0;
}

