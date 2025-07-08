#include <stdio.h>

int main() {
    printf("Q16. The current through the Zener diode in the figure is:\n\n");

    printf("(a) 33 mA\n");
    printf("(b) 3.3 mA\n");
    printf("(c) 2 mA\n");
    printf("(d) 0 mA\n\n");

    printf("Correct Answer: (c) 2 mA\n\n");

    printf("Explanation:\n");
    printf("1. The supply voltage is 10V, and the Zener voltage is 3.3V.\n");
    printf("2. The series resistor (2.2kΩ) limits the current from the supply:\n");
    printf("   I_total = (10V - 3.3V) / 2.2kΩ ≈ 3.045 mA.\n");
    printf("3. The load resistor R1 (0.1kΩ=100Ω) draws 3.3V/100Ω=33mA.\n");
    printf("4. Since the required load current is voltage drop across zener resistance divided by zener resistance \n");
    printf("   the Zener conduct, resulting in I_Z=2mA.\n");

    return 0;
}

