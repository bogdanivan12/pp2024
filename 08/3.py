file = open("3.in", "r")
l = {int(x) for x in file.readline().split()}
k = int(file.readline())
file.close()

nr_bune = [x for x in l if len(str(x)) >= k]
print(sorted(nr_bune))
