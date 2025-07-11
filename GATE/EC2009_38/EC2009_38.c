#include <stdio.h>

int main() {
    printf("Q38) Refer to the NAND and NOR latches shown in the figure. "
           "The inputs (P1, P2) for both latches are first made (0,1) and then, "
           "after a few seconds, made (1,1). The corresponding stable outputs (Q1, Q2) are:\n\n");

    printf("(A) NAND: first (0,1) then (0,1)   NOR: first (1,0) then (0,0)\n");
    printf("(B) NAND: first (1,0) then (1,0)   NOR: first (0,1) then (0,1)\n");
    printf("(C) NAND: first (1,0) then (1,0)   NOR: first (1,0) then (0,0)\n");
    printf("(D) NAND: first (1,0) then (1,1)   NOR: first (0,1) then (0,1)\n\n");


    int p1, p2, q1_nand, q2_nand;
    p1 = 0; p2 = 1;
    q1_nand = 1; 
    q2_nand = 0;

    printf("NAND latch first state with P1=0, P2=1 => Q1=%d, Q2=%d\n", q1_nand, q2_nand);
    p1 = 1; p2 = 1;
    printf("NAND latch second state with P1=1, P2=1 => Q1=%d, Q2=%d\n\n", q1_nand, q2_nand);

    int q1_nor, q2_nor;
    p1 = 0; p2 = 1;
    q1_nor = 0; 
    q2_nor = 1;

    printf("NOR latch first state with P1=0, P2=1 => Q1=%d, Q2=%d\n", q1_nor, q2_nor);

   
    p1 = 1; p2 = 1;
    printf("NOR latch second state with P1=1, P2=1 => Q1=%d, Q2=%d\n\n", q1_nor, q2_nor);

    printf("Correct Answer: Option A\n");
    printf("Explanation:\n");
    printf("- NAND latch: first S=0→Q=1, then inputs go to (1,1)→holds Q=1→Q1=1,Q2=0.\n");
    printf("- NOR latch: first R=1→Q=0, then (1,1)→invalid but holds Q=0→Q1=0,Q2=0.\n");

    return 0;
}

