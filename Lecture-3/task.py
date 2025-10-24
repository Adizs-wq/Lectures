c = 0
i = 1
min = -2000
max = 2000
if min < 0 and max < 0:
    e = min - max
elif min > 0 and max > 0:
    e = max - min
else:
    e = abs(min) + max

while True:
    print("<,>,==?, стартуем с 0")
    d = input()
    if d == "<":
        c -= (e/2/i)
        i += 1
        print(int(c))
        continue
    elif d == ">":
        c += abs((e/2/i))
        i += 1
        print(int(c))
        continue
    elif d == "==":
        print("Победа!")
        break
    else:
        print("Белеберду не пиши")
        break
        