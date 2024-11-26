n = int(input())
mat = [[n * i + j for j in range(1, n + 1)] for i in range(n)]
[print(" ".join([str(x) for x in mat[i]])) for i in range(n)]
