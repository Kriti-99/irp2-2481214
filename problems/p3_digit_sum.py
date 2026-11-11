def digit_sum(n):
    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)


num = int(input("Enter a number: "))

result = digit_sum(abs(num))

print("Sum of digits:", result)
