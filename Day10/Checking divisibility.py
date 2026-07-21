num = int(input("Enter a number: "))
divisors = [3, 5, 7, 9, 11]

print(Divisibility Results for {num}")
for d in divisors:
    if num % d == 0:
        print(f"✓ Divisible by {d}")
    else:
        print(f"✗ Not divisible by {d}")
