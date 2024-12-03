file_in = open("test.in", "r")
file_out = open("test.out", "w")

nota = 1
for i in range(9):
    exercitiu = file_in.readline().strip()
    x, y, z = [int(nr) for nr in exercitiu.replace("*", "=").split("=")]
    file_out.write(f"{exercitiu} ")
    if x * y == z:
        file_out.write("Corect\n")
        nota += 1
    else:
        file_out.write(f"Gresit {x * y}\n")
file_in.close()

file_out.write(f"Nota: {nota}")
file_out.close()
