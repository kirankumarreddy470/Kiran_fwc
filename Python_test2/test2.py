#1 Printing hello world
print("Hello World");


#2 Sum of two numbers
a=5;
b=10;
x=a + b;
print("The sum of two numbers is:",x);



#3 Finding largest number
a=int(input("Enter the 1st number:"));
b=int(input("Enter the 2nd number:"));
c=int(input("Enter the 3rd number:"));
y=max(a,b,c);
print("The largest number is:",y);



#4 Program to find given number is even or odd
a=int(input("Enter the number:"));
if (a%2 == 0):
    print("Given number is even");
else :
    print("Given number is odd");
    
    
#5 Sum of total numbers in a list
lst=[2,4,6,56,32];
sum=0;
for i in range (len(lst)):
    sum=sum+lst[i];
print("The sum of total numbers in a list is:",sum);


#6 Fibonacci series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
t = int(input("Enter the number of terms: "));
print("Fibonacci series:");
for i in range(t):
    print(fibonacci(i), end=" ");
print();  


#7 Temperature from celsius to fahrenciet
cel = float(input("Enter temperature in Celsius: "));
fah = (cel * 9/5) + 32;
print(f"{cel}°C is equals to {fah}°F");



#8 Factorial of given number
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



#9 Program to check if a number is prime
num = int(input("Enter a number: "));
if (num > 1):
    for i in range(2,num):
        if (num % i) == 0:
            print("Given number is not a prime number");
            break;
    else:
        print("Given number is a prime number");
else:
    print("Given number is not a prime number");




#10 Program to find the GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a;
num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));
gcd1 = gcd(num1, num2);
print("The GCD of", num1, "and", num2, "is", gcd1);




#11 Get user input
text = input("Enter a string: ");
reverse = "";
for i in text:
    reverse = i + reverse;
print("Reversed string:", reverse);



#12. Write a program to find the sum of the digits of a given number.
tex = int(input("Enter a number: "));
add = 0;
while tex > 0:
    digit = tex % 10;
    add += digit;
    tex //= 10;
print("Sum of digits:", add);


#13. Write a program to check whether a given string is a palindrome or not.
text = input("Enter a string: ");
text = text.lower();
if text == text[::-1]:
    print("The string is a palindrome.");
else:
    print("The string is not a palindrome.");




#14. Write a program to find the area of a rectangle.
length=int(input("Enter length of rectangle:"));
breadth=int(input("Enter breadth of rectangle:"));
Area=length*breadth;
print(f"Area of Rectangle:",Area);



#15. Write a program to find the area of a circle.
import math
radius=int(input("Enter the radius:"));
area=math.pi * radius ** 2;
print("area of circle",area);







































