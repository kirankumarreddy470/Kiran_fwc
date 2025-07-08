print("Q.38  Refer to the NAND and NOR latches shown in the figure. The inputs (P1, P2) for both the latches are first made (0,1) and then, after a few seconds, made  (1,1). The corresponding stable outputs (Q1, Q2) are:");
print();
print("(A) NAND: first (0,1) then (0,1)     NOR: first (1,0) then (0,0)");
print("(B) NAND: first (1,0) then (1,0)     NOR: first (1,0) then (1,0)");
print("(C) NAND: first (1,0) then (1,0)     NOR: first (1,0) then (0,0)");
print("(D) NAND: first (1,0) then (1,1)     NOR: first (0,1) then (0,1)");
print("\nSolution:");
print();

def nand(a, b):
    return int(not (a and b));

def nor(a, b):
    return int(not (a or b));


def simulate_nand_latch():
    print("NAND Latch:");
    P1, P2 = 0, 1;
    Q1 = 1;
    Q2 = nand(P2, Q1);
    Q1 = nand(P1, Q2);
    print(f"First (P1,P2)=({P1},{P2}) => (Q1,Q2)=({Q1},{Q2})");
    P1, P2 = 1, 1;
    Q2 = nand(P2, Q1);
    Q1 = nand(P1, Q2);
    print(f"Then (P1,P2)=({P1},{P2}) => (Q1,Q2)=({Q1},{Q2})\n");
    
def simulate_nor_latch():
    print("NOR Latch:");
    P1, P2 = 0, 1;
    Q1 = 0;
    Q2 = nor(P2, Q1);
    Q1 = nor(P1, Q2);
    print(f"First (P1,P2)=({P1},{P2}) => (Q1,Q2)=({Q1},{Q2})");
    P1, P2 = 1, 1;
    Q2 = nor(P2, Q1);
    Q1 = nor(P1, Q2);
    print(f"Then (P1,P2)=({P1},{P2}) => (Q1,Q2)=({Q1},{Q2})\n");
    
simulate_nand_latch();
simulate_nor_latch();

print("Correct Option:C");
