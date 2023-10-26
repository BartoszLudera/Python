import argparse

def factorize(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            count = 0
            while num % divisor == 0:
                count += 1
                num //= divisor
            factors.append((divisor, count))
        divisor += 1
    
    if num > 1:
        factors.append((num, 1))
    
    return factors

def format_factorization(factors):
    factorization = ""
    for factor, count in factors:
        if count == 1:
            factorization += f"{factor}*"
        else:
            factorization += f"{factor}^{count}*"
    
    return factorization.rstrip("*")

def main():
    parser = argparse.ArgumentParser(description="List of numbers.")
    parser.add_argument("numbers", nargs="+", type=int, help="List of numbers to factorize")

    args = parser.parse_args()
    numbers = args.numbers

    for number in numbers:
        factors = factorize(number)
        result = format_factorization(factors)
        print(f"Factorization: {number} is: {result}")

if __name__ == "__main__":
    main()
