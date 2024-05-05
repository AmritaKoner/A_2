def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two numbers
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Get user input for the upper limit of Fibonacci sequence
limit = int(input("Enter the upper limit for Fibonacci sequence: "))

# Generate Fibonacci sequence up to the specified limit
fib_sequence = fibonacci(limit)

# Print the Fibonacci sequence
print("Fibonacci sequence up to", limit, ":", fib_sequence)