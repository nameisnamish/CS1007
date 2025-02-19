def sum_of_digits(n):
    if n == 0:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number:"))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}")
