x = 0
y = 1
sum = 0
i = 0
def fib(lim) -> int:
    global x
    global y
    global sum
    global i 
    sum = x + y
    x = y
    y = sum
    print(x,y)
    i += 1
    if lim > i:
        return fib(10)
    else:
        return fib

fib(10)