#include <stdio.h>


int mux(int d0, int d1, int s) {
    return s ? d1 : d0;
}


int and_using_mux(int A, int B) {
    return mux(0, A, B);
}


int xor_using_2_muxes(int A, int B) {
    int notA = mux(1, 0, A);          
    return mux(A, notA, B);             
}

int main() {
    printf("=============================================\n");
    printf("Question:\n");
    printf("What are the minimum number of 2-to-1 multiplexers required to generate\n");
    printf("a 2-input AND gate and a 2-input Ex-OR gate?\n");
    printf("\nOptions:\n");
    printf("(A) 1 and 2\n");
    printf("(B) 1 and 3\n");
    printf("(C) 1 and 1\n");
    printf("(D) 2 and 2\n");
    printf("=============================================\n\n");

    printf("Answer: Option A (1 and 2)\n\n");

    printf("Explanation:\n");
    printf("- A 2-input AND gate can be implemented using 1 MUX:\n");
    printf("  AND(A,B) = MUX(0, A, B) -> if B=0 output 0, if B=1 output A.\n");
    printf("- A 2-input XOR gate requires generating complement ~A first, which needs 1 MUX,\n");
    printf("  and then final XOR logic implemented with another MUX, so total 2 MUXes.\n");
    printf("\nTherefore, the minimum number of 2-to-1 multiplexers required is:\n");
    printf("1 for AND and 2 for XOR -> Option A.\n");

    printf("\nTruth tables (simulated):\n");
    printf("A B | AND  XOR\n");
    printf("----------------\n");
    for (int A=0; A<=1; A++) {
        for (int B=0; B<=1; B++) {
            int and_out = and_using_mux(A, B);
            int xor_out = xor_using_2_muxes(A, B);
            printf("%d %d |  %d    %d\n", A, B, and_out, xor_out);
        }
    }
    return 0;
}

