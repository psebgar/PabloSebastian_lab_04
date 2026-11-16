def add_large(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))
        i -= 1
        j -= 1

    result_array = "".join(reversed(result)).lstrip("0")
    return result_array if result_array else "0"


def multiply_large(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    n1 = len(num1)
    n2 = len(num2)
    pos = [0] * (n1 + n2)

    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1 = i + j
            p2 = i + j + 1
            total = mul + pos[p2]
            pos[p1] += total // 10
            pos[p2] = total % 10

    result_string = "".join(map(str, pos)).lstrip("0")
    return result_string if result_string else "0"


def main():
    try:
        with open("numere.txt", "r", encoding="utf-8") as file:
            numbers = [line.strip() for line in file.read().splitlines() if line.strip()]

        if len(numbers) < 2:
            print("Error: The file must contain at least 2 numbers.")
            return

        num1, num2 = numbers[0], numbers[1]

        if not (num1.isdigit() and num2.isdigit()):
            print("Error: Both lines must contain valid non-negative integers.")
            return

        if len(num1) > 200 or len(num2) > 200:
            print("Error: Numbers must have at most 200 digits.")
            return

        num1_clean = num1.lstrip("0") or "0"
        num2_clean = num2.lstrip("0") or "0"

        total_sum = add_large(num1_clean, num2_clean)
        total_product = multiply_large(num1_clean, num2_clean)

        print(f"Number 1: {num1_clean}")
        print(f"Number 2: {num2_clean}")
        print(f"Sum: {total_sum}")
        print(f"Product: {total_product}")

    except FileNotFoundError:
        print("Error: The file 'numere.txt' doesn't exist.")


if __name__ == "__main__":
    main()
