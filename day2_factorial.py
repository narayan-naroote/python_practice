def fact(n):
    if n == 0:      # base condition
        return 1
    return n * fact(n-1)  # recursion call

print(fact(10))