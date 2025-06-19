#1 Sum and multiplication of numbers
num1=int(input("Enter the first number:"));
num2=int(input("Enter the second number:"));
x=num1 + num2;
y=num1 * num2;
print("Sum of Two numbers:",x);
print("Multiplication of Two numbers:",y);

#2 Sum of current number and previous number
num=int(input("Enter Number:"));
add=num+(num-1);
print("sum of current and previous number",add);


#3 Characters at even index
text = input("Enter a string:");
even = "";
for i in range(len(text)):
    if i % 2 == 0:
        even += text[i];
print("Characters at even indices:", even);



#4 Remove first n characters
text = input("Enter a string:");
n = int(input("Enter number of characters to remove from the start:"));
result = text[n:];
print("String after removal:", result);


#5 The First and Last Numbers of a List are the Same
lst = [10, 20, 30, 40, 10];
x=len(lst)-1;
if (lst[0] == lst[x]):
    print("The first and last numbers are the same.");
else:
    print("The first and last numbers are different.");
    
    
    
#6 Display numbers which are divisible by 5
for num in range(0,200):
    if num%5==0:
        print("Numbers which are divisible by 5 are:",num);


#7 Number of occurrence of substring in main string
main = input("Enter the main string: ");
sub = input("Enter the substring to count: ");
count = main.count(sub);
print(f"The substring '{sub}' occurs {count} time(s) in the given string");

