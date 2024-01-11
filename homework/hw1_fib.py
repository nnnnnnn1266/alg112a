##此程式使用ChatGPT+課程教材寫出，非自創

def fib(n):
    fib_nub = [0, 1]

    for i in range(2, n + 1):
        next_term = fib_nub[i - 1] + fib_nub[i - 2]
        fib_nub.append(next_term)

    return fib_nub[:n]

# test
n = 10  
result = fib(n)
print(result)
