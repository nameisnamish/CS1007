def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
