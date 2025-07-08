#include <stdio.h>

int main() {
    printf("Q36) If X=1 in the logic equation\n");
    printf("[X + Z*(~Y + (~Z + X*Y))] * [X + ~Z*(X+Y)] = 1\n");
    printf("then which of the following is true?\n\n");

    printf("(A) Y=Z\n");
    printf("(B) Y=~Z\n");
    printf("(C) Z=1\n");
    printf("(D) Z=0\n\n");

    printf("Explanation:\n");
    printf("- First term: A=X+Z*(~Y+(~Z+X~Y)) with X=1 makes A=1 always (1+anything=1).\n");
    printf("- Second term: B=~X+~Z*(X+Y) with X=0 also always gives B=Z~ (0+~Z=~Z).\n");
    printf("- Therefore, the equation holds for any Y,Z values. But among the options,\n");
    printf("  the simplest relation matching the options without conflict is  (~Z=1)Z=0.\n");

    printf("\nCorrect Answer: Option D (Z=0)\n");

    return 0;
}


