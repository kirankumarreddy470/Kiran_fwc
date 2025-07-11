def print_kmap():
    pq_labels = ["00", "01", "11", "10"]
    rs_labels = ["00", "01", "11", "10"]

    kmap = [
        [0, 1, 0, 0], 
        [1, 1, 1, 1],
        [1, 1, 1, 0],  
        [0, 0, 1, 0],  
    ]

    print("8. The minimal sum-of-products expression for the logic function f represented")
    print("   by the given Karnaugh map is:\n")
    print("  PQ")
    print("       " + "  ".join(pq_labels))
    print("RS")
    for i, row in enumerate(kmap):
        print(f" {rs_labels[i]}    {'   '.join(map(str, row))}")


    print("\nOptions:")
    print(" (A)  QS + P'R'S + PQR + P'RS + PQ'R'")
    print(" (B)  QS + P'R'S + PQ'R + P'RS + PQ'R'")
    print(" (C)  P'R'S + PQ'R + P'RS + PQ'R'")
    print(" (D)  P'R'S + PQR + P'RS + PQ'R'\n")

    print("Correct Answer: Option (D)")
    print("Minimal SOP expression: P'R'S + PQR + P'RS + PQ'R'")

print_kmap()
