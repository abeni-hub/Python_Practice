cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]
    
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
