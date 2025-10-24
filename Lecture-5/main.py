x = 0

def print_to_concol(b):
    global x
    x += 1
    b *= 3
    print("Hello World", x, b)
    return print_to_concol


print_to_concol(2)
print_to_concol(5)

def rec(x: int) -> int:
    print(x)
    x += 1
    return rec(x)

rec(0)