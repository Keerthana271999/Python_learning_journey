total = 0
for number in range(101):
    if number % 2 == 0:
        total += number
print(f"sum of even numbers (1-100): {total}")

total = 0
for number in range(2, 101, 2):
    total += number
print(f"sum of even numbers (1-100): {total}")
