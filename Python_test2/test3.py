#1 Get input as a list of integers
arr = list(map(int, input("Enter the elements of the array using space: ").split()));
arr1 = list(set(arr));
if len(arr1) < 2:
    print("Array does not have a second largest element.")
else:
    arr1.sort(reverse=True);
    print("The second largest element is:",arr1[1]);
  
  
  
#2
arr = list(map(int, input("Enter elements: ").split()));
arr.sort();
print("Sorted list in ascending order:", arr)


#3
# Get input from the user
arr = list(map(int, input("Enter elements: ").split()));
arr2 = [];
for item in arr:
    if item not in arr2:
        arr2.append(item);
print("List after removing duplicates:", arr2);



#4
lst1 = list(map(int, input("Enter elements of the first list : ").split()));
lst2 = list(map(int, input("Enter elements of the second list : ").split()));
common = [];
for i in lst1:
    if i in lst2 and i not in common:
        common.append(i);
print("Common elements:", common);


#5 Factorial of number using recursion
def factorial(n):
    if n == 0 or n==1 :
        return 1
    else :
        return n* factorial(n-1)
num=int(input("Enter the number:"));
if num < 0:
    print("Factorial doesn't exist for negative number");
else :
    print(f"Factorial of given {num} is {factorial(num)}");



#6. Write a program to find the LCM of two numbers.
def lcm(a, b):
    lcm1 = max(a, b)
    while True:
        if lcm1 % a == 0 and lcm1 % b == 0:
            return lcm1
        lcm1 += 1;
num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));



#7 Binary search
input_str = input("Enter sorted elements (space-separated): ")

# Manually split string by spaces (without using split)
arr = []
temp = ""
for ch in input_str:
    if ch != ' ':
        temp += ch
    else:
        if temp != "":
            arr.append(int(temp))
            temp = ""
# Append last number
if temp != "":
    arr.append(int(temp))

# Get target to search
target_str = input("Enter the element to search: ")
target = int(target_str)

# Binary search implementation
left = 0
right = len(arr) - 1
result = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        result = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if result != -1:
    print("Element", target, "found at index", result)
else:
    print("Element", target, "not found in the list")


#8 Write a program to implement selection sort.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index where target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage:
sorted_list = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the target number to search: "))

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")


#9. Write a program to implement merge sort.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]   # Dividing the array elements
        right_half = arr[mid:]

        merge_sort(left_half)   # Sort the first half
        merge_sort(right_half)  # Sort the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Get input from user
elements = list(map(int, input("Enter numbers separated by spaces: ").split()))

merge_sort(elements)

print("Sorted list:", elements)



#10. Write a program to implement quick sort.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list of zero or one element is sorted

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]   # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quick_sort to left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)

# Get input from user
elements = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_elements = quick_sort(elements)
print("Sorted list:", sorted_elements)


#11 Simple function to check primality
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
start = int(input("Enter the start number: "));
end = int(input("Enter the end number: "));
total = 0;
for num in range(start, end + 1):
    if is_prime(num):
        total += num;
print(f"Sum of prime numbers between {start} and {end} is {total}");


#12 Get input numbers
start = int(input("Enter the start number: "));
end = int(input("Enter the end number: "));
total = 0;
for num in range(start, end + 1):
    if num % 2 == 0:
        total += num;
print(f"Sum of even numbers between {start} and {end} is {total}");


#13
start = int(input("Enter the start number: "));
end = int(input("Enter the end number: "));
total = 0;
for num in range(start, end + 1):
    if num % 2 != 0:
        total += num;
print(f"Sum of odd numbers between {start} and {end} is {total}");


#14. Write a program to find the square root of a number using the Newton-Raphson method.
def newton_raphson_sqrt(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.");
    if number == 0:
        return 0
    guess = number / 2.0 ;
    for _ in range(max_iterations):
        next_guess = 0.5 * (guess + number / guess);
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess;
    return guess  
num = float(input("Enter a non-negative number to find the square root: "));
try:
    sqrt_value = newton_raphson_sqrt(num);
    print(f"The square root of {num} is approximately {sqrt_value}");
except ValueError as e:
    print(e);


#15. Write a program to find the power of a number using recursion.
def power(base, exponent):
    if exponent == 0:
        return 1  
    elif exponent < 0:
        return 1 / power(base, -exponent)  
    else:
        return base * power(base, exponent - 1)

base_num = float(input("Enter the base number: "));
exp_num = int(input("Enter the exponent (integer): "));
result = power(base_num, exp_num);
print(f"{base_num} raised to the power {exp_num} is {result}");








