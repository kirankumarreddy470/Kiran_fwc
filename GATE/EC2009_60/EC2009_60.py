# Question representation in Python

print("Q.60 What are the minimum numbers of NOT gates and 2-input OR gates required to design the logic of the driver for this 7-segment display?");
print("(A) 3 NOT and 4 OR                  (B) 2 NOT and 4 OR")
print("(C) 1 NOT and 3 OR                  (D) 2 NOT and 3 OR")
print();
print("Solution:");
print("Given:");
print("A vending machine has two buttons P1 and P2. Based on the button presses, it displays:");
data=[
    ["P1", "P2", "Display"],
    [0, 0, 0],
    [1, 0, 2],
    [0, 1, 5],
    [1, 1, "E"]
]
for a in data:
    print(f"{a[0]:<5} {a[1]:<5} {a[2]:<5}");
print();

print("Each character lights up certain segments on a 7-segment display:");
row=[
    ["Digit", "Segments ON"],
    [0, "a,b,c,d,e,f"],
    [2, "a,b,d,e,g"],
    [5, "a,c,d,f,g"],
    ["E", "a,d,e,f,g"]
]
print();
for i in row:
    print(f"{i[0]:<5} {i[1]:<5}");
print();
print("Approach:We build truth tables for each (a-g) based on P1,P2 combinations, then derive Boolean expressions. Using only NOT and 2-input OR gates, AND operations are implemented via De Morgan's Law:");
print();
print("                        A.B = ~(~A + ~B)")
not_gates = 3
or_gates = 4
print("\nMinimum gates required:");
print(f"• {not_gates} NOT gates");
print(f"• {or_gates} OR gates");
print(f"Correct Answer: {not_gates} NOT and {or_gates} OR");
