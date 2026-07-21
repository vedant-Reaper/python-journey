a = input("Enter a number:")

if a == a[::-1]:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not-palindrome")
