f = open("matrice.in", "r")
m, n = [int(x) for x in f.readline().split()]
mat = []
for i in range(m):
    mat.append([int(x) for x in f.readline().split()])
f.close()

mat_t = [[0] * m for i in range(n)]
for i in range(m):
    for j in range(n):
        mat_t[j][i] = mat[i][j]

f = open("transpusa.out", "w")
for i in range(n):
    f.write(" ".join([str(x) for x in mat_t[i]]))
    f.write("\n")
f.close()
