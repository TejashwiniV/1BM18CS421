def fib(num):
    if num <= 1:
        return num
    else:
        return(fib(num-1)+fib(num-2))
    
num = int(input("Enter the number to generate fibonacci series:"))
for i in range(num):
    print(f'Fibonacci{[i]}:{fib(i)}')
