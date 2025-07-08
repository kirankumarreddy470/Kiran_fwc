# Define the multiplexer function
def mux2to1(sel, a, b):
    return b if sel else a

# Implement AND gate using 1 MUX
def and_using_mux(a, b):
    return mux2to1(a, 0, b)

# Implement NOT gate using 1 MUX
def not_using_mux(x):
    return mux2to1(x, 1, 0)

# Implement XOR gate using 2 MUXes (1 for NOT B, 1 for XOR logic)
def xor_using_mux(a, b):
    b_not = not_using_mux(b)
    return mux2to1(a, b, b_not)

# Print the question
print("Q. What are the minimum number of 2-to-1 multiplexers required to generate:")
print("   (i) a 2-input AND gate and (ii) a 2-input Ex-OR gate?\n")

# Print the options
print("Options:")
print("(A) 1 and 2")
print("(B) 1 and 3")
print("(C) 1 and 1")
print("(D) 2 and 2\n")

# Print the truth table
print("Truth Table for AND and XOR using MUXes:")
print("A B | AND | XOR")
print("----------------")
for a in [0, 1]:
    for b in [0, 1]:
        and_result = and_using_mux(a, b)
        xor_result = xor_using_mux(a, b)
        print(f"{a} {b} |  {and_result}   |  {xor_result}")

# Explanation and final answer
print("\nExplanation:")
print("AND gate: A single 2-to-1 MUX can implement A·B by using A as select, inputs = 0 and B → Needs 1 MUX.")
print("XOR gate: Requires NOT B (needs 1 MUX) and A as select with inputs B and NOT B → Needs 2 MUXes.")
print("\nCorrect Answer: Option (A) → 1 and 2")
