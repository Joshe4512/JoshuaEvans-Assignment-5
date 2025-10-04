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

