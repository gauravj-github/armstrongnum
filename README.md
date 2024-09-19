Armstrong Number Check
Overview:
This Python script checks whether a given number is an Armstrong number. An Armstrong number (also known as a narcissistic number) for a given number of digits is a number that is equal to the sum of its own digits raised to the power of the number of digits.

In this code, the Armstrong number condition is checked for a 3-digit number, where each digit of the number is cubed, and the sum of these cubes is compared to the original number.

Code Breakdown:
Initialization:

python
Copy code
a = 111
p = a
i = 0
sum = 0
a: Holds the number to be checked (111 in this case).
p: A copy of the original number to compare at the end.
i: A variable to temporarily store each digit.
sum: Accumulates the sum of cubes of each digit.
While Loop:

python
Copy code
while a > 0:
    i = a % 10        # Extracts the last digit of 'a'.
    sum = sum + (i * i * i)   # Adds the cube of the digit to 'sum'.
    a = a // 10       # Removes the last digit from 'a'.
The loop extracts digits from the number one by one, cubes them, and adds the cubes to sum. It continues until a becomes 0.
Condition Check:

python
Copy code
if p == sum:
    print("number is armstrong number")
else:
    print("number is not arm strong numnber")
After calculating the cube sum, the code checks if the original number (p) is equal to the sum of the cubes of its digits (sum).
If they are equal, the number is an Armstrong number, and the message "number is armstrong number" is printed.
Otherwise, it prints "number is not armstrong number".
Example:
For the number 111, the cube sum of its digits is:

1^3 + 1^3 + 1^3 = 1 + 1 + 1 = 3.
Since 3 is not equal to 111, the code will output:

typescript
Copy code
number is not armstrong number
Notes:
This code only checks for Armstrong numbers with three digits. If you want to check for larger or smaller numbers, you may need to modify the code to raise each digit to the power corresponding to the number of digits.
