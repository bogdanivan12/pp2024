x = float(input("x = "))
y = float(input("y = "))

if x == 0:
    if y == 0:
        print("ORIGINE")
    else:
        print("AXA OY")
elif y == 0:
    print ("AXA OX")
elif x == y:
    print("PRIMA BISECTOARE")
elif x == -y:
    print("A DOUA BISECTOARE")
else:
    print("IN AFARA LINIILOR PRINCIPALE")
    if x > 0 and y > 0:
        print("CADRANUL I")
    elif x < 0 and y > 0:
        print("CADRANUL II")
    elif x < 0 and y < 0:
        print("CADRANUL III")
    else:
        print("CADRANUL IV")
