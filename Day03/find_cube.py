def find_cube(number):
    return number ** 3

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = find_cube(num)
    print(f"The cube of {num} is: {result}")
