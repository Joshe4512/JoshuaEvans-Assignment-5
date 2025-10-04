# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
n = current_number
steps = 0
sequence = [current_number]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1

    sequence.append(n)
    steps += 1

print("Sequence: ", end="")
for num in sequence:
    print(num, end=" ")
print()
print(f"Steps: {steps}")
print()

# === Challenge 2: Prime Number Checker ===
print("=== Challenge 2: Prime Number Checker ===")
n = int(input("Enter a number: "))
is_prime = True

if n <= 1:
    print(f"{n} is not prime (must be greater than 1).")
    is_prime = False
elif n == 2:
    print("2 is prime!")
    is_prime = False

if is_prime:
    print(f"Testing divisors from 2 to {n - 1}...")

    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            print(f"{n} is not prime (divisible by {divisor})")
            break

    if is_prime:
        print(f"{n} is prime!")

print()

