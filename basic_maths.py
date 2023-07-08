def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

input_number = 13
if is_prime(input_number):
    print(input_number, "is a prime number.")
else:
    print(input_number, "is not a prime number.")






def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

input_number = 5
factorial_result = factorial(input_number)
print("Factorial of", input_number, "is", factorial_result)









def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

input_number = 5
fibonacci_sequence = fibonacci(input_number)
print(fibonacci_sequence)











