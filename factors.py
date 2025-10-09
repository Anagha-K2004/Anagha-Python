def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    print("Factors of", num, "are:", find_factors(num))
