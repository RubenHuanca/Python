def sum(n):
    if n <= 1:
        return 1
    else:
        return n + sum(n-1)

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calling the functions
n = 6
print(sum(n))
print(fibonacci(n))