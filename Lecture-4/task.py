# n = int(input())

# a : list = [0]*(1+2*n)

# for i in range (n,1,-1):
#     output=""
#     flip = 1
#     stroke = " " * (i-1)
#     for j in range(0,1+2*(n-i)):
#         if flip == 1:
#             output+=("a")
#         else:
#             output+=(" ")
#         flip=flip*-1
#     print(stroke, output, stroke)
    
    
n = int(input())
triangle = []

for i in range (n):
    output=""
    stroke = " " * (n-i)
    row = [1] * (i + 1)
    if i > 1:
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
    output+=(" ")
    for j in range(0,i+1):
        output+=str(row[j])
        output+=(" ")

    res = stroke + output + stroke
    print(res)