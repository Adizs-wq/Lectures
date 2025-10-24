fib_cache = {}

def fib(n: int):
    if n in fib_cache:
        return fib_cache[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_cache[n] = fib(n-1) + fib(n-2)
        return fib_cache[n]
    
finalstring = ""
for i in range(200):
    finalstring += (str(fib(i))) + ' '
print(finalstring)

