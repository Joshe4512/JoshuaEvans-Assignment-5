# JoshuaEvans Assignment-5
This repository contains solutions to three fundamental Python programming challenges: the Collatz Conjecture, a Prime Number Checker, and a Multiplication Table Generator. The solutions strictly use only Variables, Types, Expressions, Branching, and Loops.

1. Collatz Conjecture (Loop: while)
Why I Chose the while Loop
I chose a while loop for the Collatz Conjecture because the number of steps required to reach 1 is unknown and indefinite.

The loop's stopping condition is simply whether the current number (n) is equal to 1. Since we don't know if it will take 5 steps or 500 steps, a while loop is the perfect control structure:

while n != 1:
    
How the Solution Works
Initialization: The script takes the starting number (start_n) and initializes the mutable variable (n) and the step counter (steps).

Core Logic: The while loop runs as long as n is greater than 1.

Branching: Inside the loop, the if n % 2 == 0 statement checks if n is even.

If Even, n is divided by 2 (n // 2).

If Odd, n is calculated as 3n+1.

Tracking: The new value of n is appended to the sequence list, and steps is incremented.

Output: A for loop is used to iterate through the final sequence list, printing each number separated by a space, which avoids the use of the .join() string method (if that was a forbidden concept).

2. Prime Number Checker (Loop: for)
Why I Chose the for Loop
I chose a for loop because the range of numbers that must be checked is known and definite.

To check if a number n is prime, we only need to test divisors from 2 up to n−1. This is a clearly defined, fixed sequence of numbers, which is the primary use case for a for loop combined with the range() function:

Python

for divisor in range(2, n):
   test for divisibility 
     use 'break' if found 
How the Solution Works
Initialization: The script gets the number n and sets a flag variable is_prime = True.

Edge Cases: It uses if/elif statements to immediately handle n≤1 and n=2.

Iteration and Test: The for loop iterates through every potential divisor. Inside the loop, the modulus operator (n % divisor == 0) checks for perfect division.

Efficiency and Branching: If a divisor is found, the is_prime flag is set to False, the explanation is printed, and the break keyword is used to immediately stop the loop, preventing unnecessary checks.

Final Output: An if is_prime: check outside the loop determines whether the "is prime!" message should be printed (it only prints if the loop completes without hitting a break).

3. Multiplication Table Grid (Loop: for - Nested)
Why I Chose Nested for Loops

I chose nested for loops because the problem involves generating a grid of numbers. We need to control two axes:

Outer Loop (Rows): The first loop controls the vertical position (the row number). It dictates when the code moves to the next line.

Inner Loop (Columns): The second loop, nested inside the first, controls the horizontal position (the products within that row). It executes completely for every single iteration of the outer loop.

How the Solution Works
Header: A for loop first prints the column headers (1-10), using an f-string (f"{i:4}") to ensure each number takes up 4 characters for perfect spacing.

Row Loop: The outer for row_num in range(1, 11) loop begins.

Inner Loop: The inner for col_num in range(1, 11) loop calculates the product = row_num * col_num.

Formatting: Both loops rely heavily on the f"{value:4}" formatting and the print(..., end="") parameter to print the grid elements side-by-side with consistent spacing.

AI Assistance Used
This project utilized Gemini to assist 
Algorithm loop Confirmation: AI helped assist in explaining and comparing and contrasting while and for loop,s which helped pick the while loop for part 1
Coding Guidance: AI gave me tips to keep up with while using loops, such as making sure im using the right type of loops and also also to make sure that I indent the right way.


