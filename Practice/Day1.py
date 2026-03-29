# Factorial 

def factorial_iterative(n):

    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial_iterative(5))   


# Fibonacci numbers in Python

def fibonacci_list(n):
    sequence = [0, 1]
    if n <= 0: return []
    elif n == 1: return [0]
    
    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

print(fibonacci_list(10)) 