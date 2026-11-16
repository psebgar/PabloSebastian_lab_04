def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n <= 2 or n % 2 != 0:
        print("Error: the number must be an even integer larger than 2.")
        return

    pairs = []
    for p in range(2, (n // 2) + 1):
        q = n - p
        if prime(p) and prime(q):
            pairs.append(f"{p} + {q}")

    print(f"Goldbach decompositions for {n}:")
    for pair in pairs:
        print(pair)


if __name__ == "__main__":
    main()